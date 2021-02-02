class OwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt

print('Чтобы закончить введите stop')
list_data = []

flag = 'run'
while flag == 'run':
    inp_data = input('Введите число: ')
    try:
        if inp_data == 'stop':
            flag = 'stop'
            break
        elif inp_data.isdigit():
            list_data.append(int(inp_data))
        else:
            raise OwnErr('Нужно ввести число!')
    except OwnErr as err:
        print(err)

print(*list_data, sep=", ")
