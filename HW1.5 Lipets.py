firm_proceeds = float(input('Выручка фирмы? '))
firm_costs = float(input('Издержки фирмы? '))
if firm_proceeds > firm_costs:
    rent = firm_proceeds / firm_costs
    print(f'Фирма работает с прибылью, рентабельность выручки {rent}')
    n = int(input('Количество сотрудников фирмы? '))
    print(f'Прибыль в расчете на одного сотрудника {firm_proceeds / n}')
else: print('Фирма работает в убыток')
