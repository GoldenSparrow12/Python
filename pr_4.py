class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imaginary)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"


c1 = Complex(1, -33)
c2 = Complex(1, -100)
print(c1 + c2)
print(c1 * c2)
