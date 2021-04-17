# x = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_x = []
# i = 1
# while i < len(x):
#     if x[i] > x[i-1]:
#         new_x.append(x[i])
#     i += 1
# print(new_x)

x = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_x = [x[i] for i in range(1, len(x)) if x[i] > x[i-1]]
print(new_x)
