my_list = []
s = '0'
print('Чтобы закончить ввод элеметов списка введите 0')
while True:
    el = input('Введите элемент списка: ')
    if el == s:
        break
    else:
        my_list.append(el)
print(f'Введенный список {my_list}')
my_list1 = my_list.copy()
n = int(len(my_list1))
i = 0
if n % 2 == 0:
    while i < n:
        my_list1[i], my_list1[i + 1] = my_list1[i + 1], my_list1[i]
        i = i + 2
elif n % 2 == 1:
    while i < n-1:
        my_list1[i], my_list1[i + 1] = my_list1[i + 1], my_list1[i]
        i = i + 2
print(f'Измененный список {my_list1}')
