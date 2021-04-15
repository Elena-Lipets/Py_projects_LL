month_n = int(input('Введите номер месяца (число от 1 до 12) '))
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
list4 = [10, 11, 12]
if month_n in list1:
    print('зима')
elif month_n in list2:
    print('весна')
elif month_n in list3:
    print('лето')
elif month_n in list4:
    print('осень')
else: print('некорректное значение')

