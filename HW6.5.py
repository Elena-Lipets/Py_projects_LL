class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашем')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')


a = Pen('Parker')
b = Pencil('Cohinor')
c = Handle('Маркер')

a.draw()
b.draw()
c.draw()