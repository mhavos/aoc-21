inf = float("inf")

class Intervalac:
    def __init__(self, degree=3, next=None):
        self.degree = degree
        if self.degree == 0:
            self.on = 0
            return
        self.bounds = (-inf, inf)

        self.split = None
        if next is None:
            self.next = Intervalac(degree=self.degree-1)
        else:
            self.next = next

    def __repr__(self):
        if self.degree == 0:
            return f"{self.on}"
        elif self.degree == 1 and self.split is None:
            return f"{self.next.on}"
        elif self.split is None:
            return f"[{'1' if repr(self.next) == '0-(z0)-1-(z1)-0' else self.next}]"
        else:
            return f"{self.children[0]}-({'wzyx'[self.degree]}{self.split})-{self.children[1]}"

    def count(self, slices):
        if self.degree == 0:
            return self.on
        index = slices.pop()
        if index.stop <= index.start:
            return 0
        if self.split is None:
            count = self.next.count(slices.copy())
            if count == 0:
                return 0
            else:
                return (min(index.stop, self.bounds[1]) - max(index.start, self.bounds[0])) * count

        newindex = [slice(index.start, self.split), slice(self.split, index.stop)]
        return self.children[0].count(slices + [newindex[0]]) + self.children[1].count(slices + [newindex[1]])

    def set(self, slices, value):
        if self.degree == 0:
            self.on = value
            return
        index = slices.pop()
        if index.stop <= index.start:
            return
        if self.split is not None:
            newindex = [slice(index.start, min(self.split, index.stop)), slice(max(self.split, index.start), index.stop)]
            self.children[0].set(slices + [newindex[0]], value)
            self.children[1].set(slices + [newindex[1]], value)
            return

        if self.bounds[0] < index.start < self.bounds[1]:
            self.children = [self.copy(), self.copy()]
            self.split = index.start
            self.children[0].bounds = (self.bounds[0], self.split)
            self.children[1].bounds = (self.split, self.bounds[1])

            newindex = slice(self.split, index.stop)
            self.children[1].set(slices + [newindex], value)
            self.next = None
            return
        if self.bounds[0] < index.stop < self.bounds[1]:
            self.children = [self.copy(), self.copy()]
            self.split = index.stop
            self.children[0].bounds = (self.bounds[0], self.split)
            self.children[1].bounds = (self.split, self.bounds[1])

            newindex = slice(index.start, self.split)
            self.children[0].set(slices + [newindex], value)
            self.next = None
            return

        self.next.set(slices, value)

    def copy(self):
        other = Intervalac(self.degree)
        if self.degree == 0:
            other.on = self.on
            return other

        other.bounds = self.bounds

        if self.split is not None:
            other.split = self.split
            other.children = [self.children[0].copy(), self.children[1].copy()]
        else:
            other.next = self.next.copy()

        return other

    def __getitem__(self, index):
        if type(index) == int:
            index = slice(index, index+1)
        return self.handler()[index]
    def handler(self):
        return Handler(self)

    def draw(self, canvas, coords=()):
        if self.degree == 0:
            color = self.on*"red"
            #canvas.create_rectangle(coords[0][0]*k, coords[1][0]*k, coords[0][1]*k, coords[1][1]*k, fill=color)
            cube(canvas, coords, color)
        elif self.split is not None:
            for child in self.children[::-1]:
                child.draw(canvas, coords)
        else:
            self.next.draw(canvas, coords + (self.bounds,))

class Handler:
    def __init__(self, intervalac):
        self.intervalac = intervalac
        self.degree = intervalac.degree
        self.slices = []

    def __getitem__(self, index):
        if type(index) == int:
            index = slice(index, index+1)
        self.degree -= 1
        self.slices.append(index)
        return self

    def __setitem__(self, index, value):
        if type(index) == int:
            index = slice(index, index+1)
        self.degree -= 1
        self.slices.append(index)
        self.intervalac.set(self.slices[::-1], value)

    def count(self):
        return self.intervalac.count(self.slices[::-1])

intervalac = Intervalac()
with open("22in.txt", "r") as file:
    for line in file:
        action, coords = line.split()
        coords = [slice(int(dim.split("=")[1].split("..")[0]), int(dim.split("=")[1].split("..")[1])+1) for dim in coords.split(",")]
        intervalac.set(coords[::-1], int(action == "on"))

#intervalac[0:18][7:12][0] = 1
#intervalac[1:7][0:13][0] = 1
#intervalac[4:17][5:8][0] = 0
#intervalac[9:14][2:6][0] = 0
#intervalac[5:13][4:11][0] = 0

#intervalac[10:13][10:13][10:13] = 1
#intervalac[11:14][11:14][11:14] = 1
#intervalac[9:12][9:12][9:12] = 0
#intervalac[10:11][10:11][10:11] = 1

#print(intervalac)
print(intervalac.count([slice(-inf, inf)]*3))

"""import tkinter
window = tkinter.Tk()
k = 1
canvas = tkinter.Canvas(window, width=800, height=600)
canvas.pack()

def cube(canvas, coords, color):
    x, y, z = coords
    x, y, z = (10*x[0], 10*x[1]), (10*y[0], 10*y[1]), (10*z[0], 10*z[1])
    # bottom left line
    canvas.create_line(y[0] + x[0]/2, z[0] + x[0]/2, y[0] + x[1]/2, z[0] + x[1]/2)
    # front face
    for x0 in x:
        canvas.create_rectangle(y[0] + x0/2, z[0] + x0/2, y[1] + x0/2, z[1] + x0/2, fill=color)
    # right face
    canvas.create_polygon(y[1] + x[0]/2, z[0] + x[0]/2, y[1] + x[1]/2, z[0] + x[1]/2, y[1] + x[1]/2, z[1] + x[1]/2, y[1] + x[0]/2, z[1] + x[0]/2, fill=color)
    # top face
    canvas.create_polygon(y[0] + x[0]/2, z[1] + x[0]/2, y[0] + x[1]/2, z[1] + x[1]/2, y[1] + x[1]/2, z[1] + x[1]/2, y[1] + x[0]/2, z[1] + x[0]/2, fill=color)

intervalac.draw(canvas)

canvas.mainloop()"""
