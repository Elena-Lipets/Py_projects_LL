n = 5

def fact(n):
    res = 1
    for k in range(1, n+1):
        res = res * k
        yield res

for el in fact(n):
    print(el)

