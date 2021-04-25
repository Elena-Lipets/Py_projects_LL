from time import time

class TrafficLight:
    __color = None

    def running(self):
        # Пусть продолжительность состояния "красный" - 7 с, "желтый" - 2с, "зеленый" - 5с
        # Полный цикл - 7+2+5 = 14с
        t = time() % 14
        color_list = ['красный', 'желтый', 'зеленый']
        if 0 <= t < 7:
            self.__color = color_list[0]
        elif 7 <= t < 9:
            self.__color = color_list[1]
        else: self.__color = color_list[2]

a = TrafficLight()
a.running()
print(a._TrafficLight__color)
