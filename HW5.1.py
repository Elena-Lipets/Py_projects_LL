while 1:
    with open('text_5.1.txt', 'a') as a:
        line = input('Напишите что-нибудь компьютеру... конец ввода - пустая строка ')
        if line == '': break
        a.writelines(line+'\n')

