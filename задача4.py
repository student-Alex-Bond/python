def my_func(var_1, var_2):
    res = var_1 ** var_2
    return print(f'{var_1} в степени {var_2} равна {res:.3}')


def my_func_1(var_1, var_2):
    i = 1
    res = var_1
    while i < abs(var_2):
        res_1 = (res * var_1)
        res = res_1
        i = i + 1
    res_1 = 1 / res
    return print(f'{var_1} в степени {var_2} равна {res_1:.3}')


num_1 = float(input('Введите действительное положительное число :'))
num_2 = int(input('Введите отрицательную степень:'))
print('Результат через встроенную функцию')
my_func(var_1=num_1, var_2=num_2)
print('Результат чере цикл ')
my_func_1(var_1=num_1, var_2=num_2)
