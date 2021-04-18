result = {}

with open('text_5.6.txt', 'r') as a:
    for line in a.readlines():
        key = line.split(':')[0]

        b = line.split()
        i = 1
        hours = 0
        while i < len(b):
            if b[i][0] == '-':
                i += 1
                continue
            hours_str = ''
            for j in range(0, b[i].find('(')):
                hours_str += b[i][j]
            hours += int(hours_str)
            i += 1
        result.update({key: hours})
print(result)

