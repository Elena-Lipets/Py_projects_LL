def user_info(name='Name', surname='Surname', year_of_birth='0001', hometown='Earth',
              email='___@__', telephone_n=80000000000):
    record = {'name': name, 'surname': surname,
            'year_of_birth': year_of_birth, 'hometown': hometown,
            'email': email, 'telephone_n': telephone_n}
    print(record)

user_info(name='Aaa', surname='Bbb', year_of_birth='1012')
