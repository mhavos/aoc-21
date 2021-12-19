import warnings
matrixcheck = True

def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

class Semiring:
    def __init__(self, add=addition, mul=multiplication, zero=0, one=1):
        self.add = add
        self.mul = mul
        self.zero = zero
        self.one = one

class Matrix:
    __slots__ = ["m", "n", "semiring", "data"]
    default = Semiring(addition, multiplication)

    def __init__(self, m, n, data=None, semiring=None, identity=None, check=matrixcheck):
        self.m, self.n = m, n

        if semiring is None:
            semiring = Matrix.default
        self.semiring = semiring

        self.data = list()
        if data is not None:
            for m in range(self.m):
                m %= len(data)
                self.data.append(list())
                for n in range(self.n):
                    n %= len(data[m])
                    self.data[-1].append(data[m][n])
        else:
            if identity is None:
                identity = (self.m == self.n)
            for m in range(self.m):
                self.data.append(list())
                for n in range(self.n):
                    self.data[-1].append(self.semiring.one if ((m == n) and identity) else self.semiring.zero)

        if check:
            self.check()

    def check(self):
        add_fail = False
        for m in range(self.m):
            for n in range(self.n):
                if self.semiring.add(self.semiring.zero, self[m][n]) != self[m][n]:
                    add_fail = True
                    example = self[m][n]
                    break
            if add_fail:
                break
        if add_fail:
            warnings.warn(f"additive identity behaves incorrectly, such as `{self.semiring.zero} add {example} != {example}`. Change semiring.zero to a more appropriate value.",
                    category=warnings.Warning)

        mul_fail = False
        for m in range(self.m):
            for n in range(self.n):
                if self.semiring.mul(self.semiring.one, self[m][n]) != self[m][n]:
                    mul_fail = True
                    example = self[m][n]
                    break
            if mul_fail:
                break
        if mul_fail:
            warnings.warn(f"multiplicative identity behaves incorrectly, such as `{self.semiring.one} mul {example} != {example}`. Change semiring.one to a more appropriate value.",
                    category=warnings.Warning)

        if add_fail or mul_fail:
            warnings.warn(f"to turn warnings off, either set matrixcheck to False (this will turn warnings off permanently), or pass a `check=False` kwarg to matrix creation.",
                    category=warnings.Warning)

    def transpose(self):
        result = Matrix(self.n, self.m, semiring=self.semiring)
        for r in range(self.n):
            for s in range(self.m):
                result[r][s] = self[s][r]
        return result

    def __getitem__(self, key):
        return self.data[key]

    def __eq__(self, other):
        if self.m != other.m or self.n != other.n:
            return False
        for m in range(self.m):
            for n in range(self.n):
                if self[m][n] != other[m][n]:
                    return False
        return True

    def __add__(self, other):
        if type(other) != type(self): raise TypeError("cannot add a non-matrix object to a matrix")
        if self.semiring is not other.semiring: raise TypeError("matrices must belong to the same semiring to be added")
        if self.m != other.m or self.n != other.n: raise IndexError("matrices must have identical dimensions to be added")

        sum = Matrix(self.m, self.n, semiring=self.semiring)
        for m in range(self.m):
            for n in range(self.n):
                sum[m][n] = self.semiring.add(self[m][n], other[m][n])
        return sum

    def __rmul__(self, other):
        return self * other
    def __mul__(self, other):
        if type(other) != type(self): raise TypeError("cannot multiply a matrix by a non-matrix object")
        if self.semiring is not other.semiring: raise TypeError("matrices must belong to the same semiring to be multiplied")
        if self.n != other.m: raise IndexError("first matrix width must be equal to second matrix height to be multiplied")

        product = Matrix(self.m, other.n, semiring=self.semiring)
        for r in range(self.m):
            for s in range(other.n):
                sum = 0
                for q in range(self.n):
                    sum = self.semiring.add(sum, self.semiring.mul(self[r][q], other[q][s]))
                product[r][s] = sum
        return product

    def __pow__(self, exponent):
        if type(exponent) != int: raise TypeError("exponent")
        if exponent == 1: return self
        if self.m != self.n: raise IndexError("cannot raise non-square matrices to powers other than 1")

        total = Matrix(self.m, self.n, semiring=self.semiring)
        assert total * self == self, "cannot correctly perform powers if additive and multiplicative identities do not work correctly"
        current = self

        while exponent:
            if exponent & 1:
                total *= current
            exponent = exponent >> 1
            current *= current

        return total

    def __repr__(self):
        return format(self)

    def __format__(self, arg=""):
        if arg == "":
            arg = " >3"
        return "\n".join([f"Matrix({self.m}, {self.n}, ["] +
                ["    [ " + ", ".join([f"{{:{arg}}}".format(self[m][n]) for n in range(self.n)]) + (" ]" if m == self.m - 1 else " ],") for m in range(self.m)] +
                ["])"])

    def __len__(self):
        return self.m
