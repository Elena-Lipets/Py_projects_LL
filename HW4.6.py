# from itertools import count
# start_count = 3
# n_of_count = 10
#
# for el in count(start_count):
#     if el > n_of_count:
#         break
#     else:
#         print(el)


from itertools import cycle

my_list = ['весна', 'лето', 'осень', 'зима']
с = 0
for el in cycle(my_list):
    if с > 10:
        break
    print(el)
    с += 1


