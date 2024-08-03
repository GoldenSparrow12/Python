class Vector:

    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        j = 1
        for i in self.vec:
            str1 += f"{i}a{j} + "
            j += 1
        return str1[:-2]

    def __add__(self, other):
        newvec = []
        for i in range(len(self.vec)):
            newvec.append(self.vec[i] + other.vec[i])
        return Vector(newvec)


v1 = Vector([1, 5, 3])
v2 = Vector([2, 8, 6])
print(v1)
print(v1 + v2)
