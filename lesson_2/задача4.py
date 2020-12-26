my_str = input('Введите строку из нескольких слов, разделённых пробелами: ')
my_list = my_str.split()
for ind, el in enumerate(my_list, 1):
    if len(el) > 10:
        x = el[:10]
        print(ind, x)
    else:
        print(ind, el)
