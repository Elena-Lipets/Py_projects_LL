class Matrix:

    def __init__(self, x):
        self.x = x

    def __str__(self):
        for line in self.x:
            for el in line:
                print(el, ' ', end='')
            print('\n')
        return " "

    def __add__(self, other):
        if len(self.x) != len(other.x) or len(self.x[0]) != len(other.x[0]):
            print('Число строк и столбцов матриц не совпадает. Сложение не отпределено')
            return None
        c = []
        for i in range(0, len(self.x)):
            c.append([])
            for j in range(0, len(self.x[i])):
                c[i].append(self.x[i][j] + other.x[i][j])
        return Matrix(c)


a = Matrix([[1, 1, 1], [1, 1, 1]])
b = Matrix([[2, 2, 2], [2, 2, 2]])
c = a + b
print(c)
