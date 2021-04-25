class Worker:

    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._Worker__income.get('wage') + self._Worker__income.get('bonus')


worker1 = Position('Owl', 'Wise', 'manager', 5000)
worker2 = Position('Squirrel', 'Flying', 'worker', 500, 50)

print(worker1.position, worker1.get_full_name(), worker1.get_total_income())
print(worker2.position, worker2.get_full_name(), worker2.get_total_income())

