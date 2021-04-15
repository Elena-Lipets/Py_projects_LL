# не очень понимаю, зачем здесь списки и словари
month_n = int(input('Введите номер месяца (число от 1 до 12) '))
if 1 <= month_n <= 3:
    print('зима')
elif 4 <= month_n <= 6:
    print('весна')
elif 7 <= month_n <= 9:
    print('лето')
elif 10 <= month_n <= 12:
    print('осень')
else: print('некорректное значение')
