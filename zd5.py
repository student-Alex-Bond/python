with open('text4.txt', 'w') as f:
    my_list = list()
    m_str = str()
    n = 0
    while n == 0:
        num = input('Введите числа через пробел: ')
        my_str = num.split()
        for el in my_str:
            if el.isalpha():
                my_list.append(el)
        if len(my_list) == 0:
            n = 1
            my_list =num.split()
            m_str = ''.join(num)
            f.writelines(m_str)
            break
        else:
            my_list.clear()
            print('Вы ввели помимо чисел еще и символы')
with open('text4.txt', 'r') as fil:
    content = fil.read()
    summ = 0
    for el in content.split():
        summ = summ + float(el)
    print(f'Сумма элементов строки равна: {summ}')
    print(my_list)

