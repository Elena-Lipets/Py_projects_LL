x = '1 2 56 7 0 6'

with open("text_5.5.txt", "w+") as a:
    a.write(x)
    a.seek(0)
    y = (a.read()).split()
    print(sum(list(map(int, y))))
