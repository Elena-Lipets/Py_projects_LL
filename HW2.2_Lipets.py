list1 = input('Введите список значений в формате а б в... к ').split()
list2 = list1.copy()
i = 0
while i < len(list1)-1:
    list2[i] = list1[i+1]
    list2[i+1] = list1[i]
    i += 2
print('А мы теперь все перемешали )')
print(list2)
