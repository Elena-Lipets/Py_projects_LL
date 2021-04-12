score = [12, 8, 7, 7, 3, 2]
new_el = int(input('Введите новое натуральное число '))
for i in score:
    if new_el > i:
        score.insert(score.index(i), new_el)
        break
if new_el < score[-1]:
    score.append(new_el)
print(score)
