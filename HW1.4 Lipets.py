n = int(input('Введите целое положительное число '))
a = 10
x_max = n % 10 # x_max - максимальная цифра

while n//a > 0: a = a*10

while a > 10:
    x = n // a # x-текущая цифра цисла
    if x > x_max: x_max = x
    n = n % a
    a = a / 10

print(x_max)
