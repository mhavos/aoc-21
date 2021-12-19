from matrix.matrix import Matrix

corners = (
    (
        (0, 1, 0),
        (-1, 0, 0),
        (0, 0, 1)
    ),
)
rotate = (
    (
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, 1)
    ),
)
reflect = (
    (
        (0, 1, 0),
        (1, 0, 0),
        (0, 0, -1)
    ),
)
spinny = (
    (
        (0, 1, 0),
        (0, 0, 1),
        (1, 0, 0)
    ), (
        (0, 0, 1),
        (1, 0, 0),
        (0, 1, 0)
    )
)

transformations = [Matrix(3, 3)]
for choices in (corners, rotate, reflect, spinny):
    for trans in transformations.copy():
        for choice in choices:
            transformations.append(Matrix(3, 3, data=choice)*trans)

class Vector:
    transformations = transformations

    def __init__(self, *args):
        if len(args) == 1:
            args = args[0]

        self.data = tuple(args)

    def __add__(self, other):
        return Vector(self[i] + other[i] for i in range(3))

    def __sub__(self, other):
        return Vector(self[i] - other[i] for i in range(3))

    def quadrance(self):
        return sum(self[i]**2 for i in range(3))

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def similar_to(self, other, request=False):
        for trans in Vector.transformations:
            if self.transform(trans) == other:
                return trans if request else True
        return None if request else False

    def transform(self, trans):
        return Vector(
            sum(trans[r][s]*self[s] for s in range(3)) for r in range(3)
        )

    def __repr__(self):
        return f"Vector{self.data}"

    def __getitem__(self, index):
        return self.data[index]

    def __neg__(self):
        return Vector(-x for x in self.data)
