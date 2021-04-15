def my_func(x, y):
    if y >= 0: return None
    res = 1
    while y < 0:
        res = res / x
        y = y+1
    return res

print(my_func(2,-2))
