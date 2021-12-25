class Expression:
    def __init__(self, value=0, index=None):
        self.value = {None:value}
        if index is not None:
            self.value[index] = 1
    def __repr__(self):
        return f"{' + '.join([repr(self.value[key]) for key in self.value])}"
    def copy(self):
        new = Expression()
        new.value = self.value.copy()
        return new

    def __iadd__(self, other):
        if type(other) == int:
            self.value[None] += other
            return

        for key in other.value:
            if self.value.get(key, None) is None:
                self.value[key] = other.value[key]
            else:
                self.value[key] += other.value[key]

    def __imul__(self, other):
        if type(other) == int:
            if other == 0:
                self.value = {None:0}
                return
            for key in self.value:
                self.value[key] *= other
            return

        for key in 

with open("24in.txt", "r") as file:
    for line in file:
        pass
