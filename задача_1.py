def division(var_1, var_2):
    try:
        division = var_1 / var_2
        print(f'{division:.2}')
    except ZeroDivisionError:
        print("На ноль делить нельзя")


arg_1 = float(input('Первый аргумент: '))
arg_2 = float(input('Второй аргумент: '))
division(arg_1, arg_2)
