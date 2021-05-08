class MyExceptions(Exception):
    def __init__(self, txt):
        self.txt = txt

a, b = input('Введите 2 действительных числа через пробел ').split()

try:
    #c = int(a)/int(b)
    if int(b) == 0:
        raise MyExceptions('На ноль делить нельзя.')
except MyExceptions as err:
    print(err)
else:
    print(int(a)/int(b))

