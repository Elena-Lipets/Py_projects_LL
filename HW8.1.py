class Data:
    def __init__(self, user_input):
        Data.user_input = user_input

    @classmethod
    def str_to_number(cls, data_str):
        a = data_str.split('-')
        return list(map(int, a))

    @staticmethod
    def data_check(data_list):
        errors = []
        if ((data_list[1] in [1, 3, 5, 7, 8, 10, 12]) and (data_list[0] not in range(1, 32))) or \
                ((data_list[1] in [4, 6, 9, 11]) and (data_list[0] not in range(1, 31))) or \
                ((data_list[1] == 2) and (data_list[0] not in range(1, 29))):
            errors.append('Некорректное число')
        if data_list[1] not in range(0, 13):
            errors.append('Некорректно введен месяц')
        if data_list[2] not in range(0, 2022):
            errors.append('Некорректно введен год')
        if errors:
            print(errors)
            #raise ValueError
        else:
            print('Дата введена корректно')

print(Data.str_to_number('01-12-13'))
Data.data_check(Data.str_to_number('45-12-4390'))
