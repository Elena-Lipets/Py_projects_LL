class Storage:
    def __init__(self, name, n_of_cells):
        self.name = name
        self.n_of_cells = n_of_cells

    def to_receive(self, name, n, department):
        if type(n) != int:
            print('количество приборов должно быть целым числом. Неверно введено n')
            return None
        self.n_of_cells -= n
        return {'name': name, 'quantity': n, 'department': department}


class Technique:
    def __init__(self, name, date_of_prod, prise, is_in_storage):
        self.name = name
        self.date_of_prod = date_of_prod
        self.prise = prise
        self.is_in_storage = is_in_storage


class Printer(Technique):
    def __init__(self, name, date_of_prod, prise, is_in_storage, cartridge):
        Technique.__init__(name, date_of_prod, prise, is_in_storage)
        self.cartridge = cartridge


class Scanner(Technique):
    def __init__(self, name, date_of_prod, prise, is_in_storage, speed):
        Technique.__init__(name, date_of_prod, prise, is_in_storage)
        self.speed = speed
