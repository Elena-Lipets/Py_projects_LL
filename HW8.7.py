class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}+i{self.b}'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


print(ComplexNumber(2, 3) + ComplexNumber(5, 3))
print(ComplexNumber(1, 0) * ComplexNumber(0, 2))
