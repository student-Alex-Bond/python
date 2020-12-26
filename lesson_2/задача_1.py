my_list = []
s = '0'
print('Вводить можно целые числа, булевые значения или строки')
print('Чтобы закончить ввод элеметов списка введите 0')
while True:
    el = input('Введите элемент списка: ')
    if el == s:
        break
    elif el == 'False' or el == 'True' or el == 'false' or el == 'true':
        el = bool(el)
        my_list.append(el)
    elif el.isdigit():
        el = int(el)
        my_list.append(el)
    elif el == str(el):
        el = str(el)
        my_list.append(el)

i = 0
while i < len(my_list):
    print(f'{i + 1}-й элемент имеет тип {type(my_list[i])}')
    i = i + 1
print(f'Сам список {my_list}')
