class Matrix:
    def __init__(self, m, n, data):
        self.m, self.n = m, n

        self.data = list()
        for m in range(self.m):
            self.data.append(list())
            for n in range(self.n):
                self.data[-1].append(data[m][n])

    def __mul__(self, other):
        if self.n != other.m: raise IndexError("first matrix width must be equal to second matrix height to be multiplied")

        product = Matrix(self.m, other.n, data=[[0 for s in range(other.n)] for r in range(self.m)])
        for r in range(self.m):
            for s in range(other.n):
                for q in range(self.n):
                    product[r][s] += self[r][q] * other[q][s]
        return product

    def __pow__(self, exponent):
        if exponent == 1: return self

        total = Matrix(self.m, self.n, data=[[int(r == s) for s in range(9)] for r in range(9)])
        current = self

        while exponent:
            if exponent & 1:
                total *= current
            exponent = exponent >> 1
            current *= current

        return total

    def __getitem__(self, key):
        return self.data[key]

with open("6in.txt", "r") as file:
    ages = Matrix(9, 1, data=[[0] for i in range(9)])
    for x in file.readline()[:-1].split(","):
        age = int(x)
        ages[age][0] += 1
    print(*(ages[age][0] for age in range(9)))

    gen = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    gen = Matrix(9, 9, data=gen)
    gen256 = gen**256

    addup = Matrix(1, 9, data=[[1 for i in range(9)]])
    print((addup*gen256*ages)[0][0])
