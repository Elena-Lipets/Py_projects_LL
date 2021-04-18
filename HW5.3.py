with open('text_5.3.txt') as a:
    b = a.readlines()
    total_salary = 0
    for line in b:
        if int(line.split()[1]) < 20000: print(f'Меньше 20000 получает: {line.split()[0]}')
        total_salary += int(line.split()[1])
    print(f'Средний оклад - {total_salary / len(b)}')
