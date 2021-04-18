from json import dump

firm_dict = {}
with open('text_5.7.txt') as a:
    sum_profit = 0
    n_of_firm = 0
    for line in a.readlines():
        b = line.split()
        key = b[0]
        profit = int(b[2]) - int(b[3])
        firm_dict.update({key: profit})
        if profit > 0:
            sum_profit += profit
            n_of_firm += 1
    res_list = [firm_dict, {'average_profit': round(sum_profit / n_of_firm)}]

with open('result.json', 'w') as j_list:
    dump(res_list, j_list)
