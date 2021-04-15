sent = input('Напишите предложение ').split()
for word in sent:
    print(sent.index(word) + 1, ' ', word[:10])
