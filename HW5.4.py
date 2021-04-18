trans = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
with open('text_5.4_eng.txt', 'r') as a, open('text_5.4.txt', 'a') as b:
    for line in a.readlines():
        c = line.split()
        b.writelines([trans.get(c[0]), c[1], c[2], '\n'])



