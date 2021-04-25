class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.speed} km/h')

class TownCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60: print('Максимальная разрешенная скорость превышена')

class WorkCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40: print('Максимальная разрешенная скорость превышена')


car1 = TownCar('BMW', 'black', 110, True)
car2 = WorkCar('буханка', 'серая в яблоках', 250)

print(car1.name, car1.color)
car1.go()
car1.turn('направо')
car1.show_speed()
car1.stop()

print(car2.color, car2.name)
car2.show_speed()