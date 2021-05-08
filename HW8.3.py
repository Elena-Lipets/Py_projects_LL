class MyExceptions(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while 1:
    x = input('Введите число или завершите программу командой "stop" ')
    if x == 'stop':
        print(my_list)
        break
    try:
        if not x.isdigit():
            raise MyExceptions('Вы ввели не число')
    except MyExceptions as er:
        print(er)
    else:
        my_list.append(int(x))




