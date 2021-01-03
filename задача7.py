n = int(input('Введите num: '))


def fact(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
        yield (res)


for i in fact(n):
    print(i)
