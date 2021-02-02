class OwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt

a = input('Введите первое число: ')
b = input('Введите второе число: ')

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise OwnErr('Делитель не может быть равен 0!')
except OwnErr as err:
    print(err)
else:
    print(f'Результат деления: {round(a/b,2)}')

