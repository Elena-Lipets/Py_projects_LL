MENU = '1. Ввести новый товар\n2. Вывести данные\n3. Выход'
products = []
fields = ('name', 'price', 'quantity', 'units')
i = 1

while 1:
    print('_'*50)
    print(MENU)
    print('_' * 50)
    choice = input('Выберите пункт меню ')
    if choice == '1':
        new_product = {}
        for field in fields:
            new_product[field] = input(f'Введите значение {field} ')
        products.append(tuple([i, new_product]))
        i += 1
    elif choice == '2':
        for product in products:
            print(product)
    elif choice == '3':
        info = {}
        for field in fields:
            subsidiary_list = []
            for product in products:
                subsidiary_list.append(product[1][field])
            info.update({field: subsidiary_list})
        print('Завершение работы. Общая информация о товарах:')
        print(info)
        break
