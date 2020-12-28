def my_func(my_list1):
    my_list2 = []
    for el in my_list1:
        my_list2.append(float(el))
    my_summa = 0
    for i in my_list2:
        my_summa = my_summa + i
    return my_summa
my_list1 = []
b = 0
esp = 'e'
s = 'q'
while True:
    if esp == s:
        break
    print('Чтобы выйти введите q')
    num_1 = input('Введите числа через пробел :').split()
    my_list = list(num_1)
    for el in my_list:
        if el != s:
            my_list1.append(el)
        else:
            esp = s
            break
    a = my_func(my_list1)
    my_list1.clear()
    b = b + a
    print(b)
