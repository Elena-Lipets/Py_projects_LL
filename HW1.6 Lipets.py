import math
a = float(input('Длина маршрута в км в первый день? '))
b = float(input('Желаемая длина маршрута в км за день? '))
if b > 50:
    print('Так и сдохнуть можно ')
    b = float(input('Введите длину маршрута менее 50 км '))
# формула для n-ого члена ряда b_n=1,1^(n-1)*a, отсюда можно выразить n
print(f'Спортсмен достигнет результата на {math.ceil(math.log(b / a, 1.1))+1} день')

# Но вы ведь цикл хотели )

#a = float(input('Длина маршрута в км в первый день? '))
#b = float(input('Желаемая длина маршрута в км за день? '))
#if b > 50:
#    print('Так и сдохнуть можно ')
#    b = float(input('Введите длину маршрута менее 50 км '))
#i = 1
#while a < b:
#    a = a * 1.1
#    i = i + 1
#print(f'Спортсмен достигнет результата на {i} день')
