def my_func(var_1, var_2, var_3):
    if var_1.replace('.', '', 1).isdigit() == True and var_2.replace('.', '', 1).isdigit() == True \
            and var_3.replace('.', '', 1).isdigit() == True:
        var_1 = float(var_1)
        var_2 = float(var_2)
        var_3 = float(var_3)
        summa = (var_1 + var_2 + var_3) - min(var_1, var_2, var_3)
        return print(f'Сумма наибольших аргументов равна {summa}')
    elif var_1.replace('-', '', 1).isdigit() == True and var_2.replace('-', '', 1).isdigit() == True \
            and var_3.replace('-', '', 1).isdigit() == True:
        var_1 = float(var_1)
        var_2 = float(var_2)
        var_3 = float(var_3)
        summa = (var_1 + var_2 + var_3) - min(var_1, var_2, var_3)
        return print(f'Сумма наибольших аргументов равна {summa}')
    else:
        mini = min(var_1, var_2, var_3)
        list_1 = [var_1, var_2, var_3]
        list_1.remove(mini)
        return print(f'Сумма наибольших аргументов равна {list_1[0] + list_1[1]}')


num_1 = input('Введите первый аргумент:')
num_2 = input('Введите второй аргумент:')
num_3 = input('Введите третий аргумент:')
my_func(var_1=num_1, var_2=num_2, var_3=num_3)
