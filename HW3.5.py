x_sum = 0
flag = 0
while 1:
    x_list = input('Для получения суммы введите числа через пробел, '
              'для выхода - специальный символ ').split()
    for x in x_list:
        try:
            float(x)
        except ValueError:
            flag = 1
            break
        else:
            x_sum += float(x)
    print(x_sum)
    if flag == 1: break
