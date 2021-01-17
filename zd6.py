import re

with open('text5.txt', 'r') as f:
    list_summa = list()
    my_dict = dict()
    for el in f:
        el = re.findall(r'\d+', el)
        summa = 0
        for j in el:
            summa = summa + int(j)
        list_summa.append(summa)

print(list_summa)
with open('text5.txt', 'r') as fil:
    my_str = str()
    my_key1 = list()
    my_key = fil.read().split('\n')
    for el in my_key:
        el = el.split(" ")[0]
        el = el[:len(el) - 1]
        my_key1.append(el)
my_dict = dict(zip(my_key1, list_summa))
print(my_key1)
print(my_dict)
