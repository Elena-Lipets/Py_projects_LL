from functools import reduce

y = list(range(100, 1001, 2))

print(reduce(lambda a, b: a * b, y))

