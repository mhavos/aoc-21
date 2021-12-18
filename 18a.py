class SnailNumber:
    __slots__ = ["data", "isIterator", "index"]

    def __init__(self, text):
        # this is a horrible, horrible way to do this, please don't do this
        self.data = eval(text)
        self.isIterator = False

    def __getitem__(self, index):
        current = self.data
        for i in index:
            current = current[i]
        return current

    def __setitem__(self, index, value):
        self[index[:-1]][index[-1]] = value

    def __iter__(self):
        # don't do this. please
        iterator = SnailNumber(repr(self))
        iterator.isIterator = True
        iterator.index = None
        return iterator

    def __next__(self):
        if self.index is None:
            self.index = []
        else:
            while self.index:
                last = self.index.pop()
                if not last:
                    self.index.append(1)
                    break
            if len(self.index) == 0:
                raise StopIteration
        while type(self[self.index]) != int:
            self.index.append(0)

        return self.index.copy()

    def reduce(self):
        done = False
        while not done:
            done = True
            for index in self:
                if len(index) > 4:
                    done = False
                    index.pop()
                    prev, next = self.neighbors(index)
                    if prev is not None:
                        self[prev] += self[index + [0]]
                    if next is not None:
                        self[next] += self[index + [1]]
                    self[index] = 0
                    break
            if not done:
                continue
            for index in self:
                if self[index] > 9:
                    done = False
                    self[index] = [self[index]//2, (self[index] + 1)//2]
                    break

    def neighbors(self, index):
        prev = index.copy()
        while prev:
            if prev[-1] == 0:
                prev.pop()
            else:
                break
        if len(prev) == 0:
            prev = None
        else:
            prev[-1] = 0
            while type(self[prev]) != int:
                prev.append(1)

        next = index.copy()
        while next:
            if next[-1] == 1:
                next.pop()
            else:
                break
        if len(next) == 0:
            next = None
        else:
            next[-1] = 1
            while type(self[next]) != int:
                next.append(0)

        return prev, next

    def magnitude(self, index=[]):
        if type(self[index]) == int:
            return self[index]
        else:
            return 3*self.magnitude(index + [0]) + 2*self.magnitude(index + [1])

    def __repr__(self):
        return repr(self.data)

    def __add__(self, other):
        result = SnailNumber(f"[{self}, {other}]")
        result.reduce()
        return result

with open("18in.txt", "r") as file:
    total = None
    for line in file:
        num = SnailNumber(line)
        if total is None:
            total = num
        else:
            total += num
print(total.magnitude())
