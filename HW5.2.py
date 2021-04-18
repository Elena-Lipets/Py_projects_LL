with open('text_5.1.txt', 'r') as a:
    print(f'Количество строк в файле - {len(a.readlines())}')
    a.seek(0)
    for i, line in enumerate(a.readlines(),1):
        print(f'количество слов в строке {i} - {len(line.split())}')

