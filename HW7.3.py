class Cage:
    def __init__(self, n):
        self.n_of_cells = n

    def __add__(self, other):
        return Cage(self.n_of_cells + other.n_of_cells)

    def __sub__(self, other):
        d = self.n_of_cells - other.n_of_cells
        if d < 0:
            print('Количество ячеек в уменьшаемой клетке меньше, чем в вычитаемой. Операция не корректна')
            return None
        else: return Cage(d)

    def __mul__(self, other):
        return Cage(self.n_of_cells * other.n_of_cells)

    def __truediv__(self, other):
        return Cage(self.n_of_cells // other.n_of_cells)

    def make_order(self, n_in_row):
        a = self.n_of_cells // n_in_row
        b = self.n_of_cells % n_in_row
        print(('*'*n_in_row + '\n')*a + '*'*b)


x = Cage(17)
x.make_order(5)
