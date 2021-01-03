from itertools import count
from itertools import cycle
from sys import argv

script_name, param_1, param_2 = argv
my_list = []
a = int(param_1)
b = int(param_2)
print("count")
for el in count(a):
    if el > b:
        break
    else:
        my_list.append(el)
        print(el)
print("cycle")
c = 0
for el in cycle(my_list):
    if c > len(my_list)+5:
        break
    print(el)
    c += 1
