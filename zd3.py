with open('zp.txt', 'r') as f:
    my_dict1 = {}
    my_list1 = list()
    for line in f:
        my_list = line.split()
        my_dict = dict.fromkeys([my_list[0]], my_list[1])
        my_dict1.update(my_dict)
    val = my_dict1.values()
    summ = 0
    for el in val:
        summ = summ + float(el)
    summ = summ / len(val)
    for key, value in my_dict1.items():
        if float(value) < 20000:
            my_list1.append(key)

print(my_dict1, sep='\n')
print(f'Средняя зп сотрудников: {round(summ, 2)}')
print('Cотрудники, которые получают менее 20000: ' + ', '.join(my_list1))
