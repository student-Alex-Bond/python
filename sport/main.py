a = int(input('Введите а: '))
b = int(input('Введите b: '))
d = 0
c = 0
d = a + c
counter =1
print(f'{counter} -й день: {d:.2f} километров')
while d < b:
    c = (d / 10)
    d = c + d
    counter = counter + 1
    print(f'{counter} -й день: {d:.2f} километров')

print(f'На {counter}-ой день Вы достигните результата - не менее {b} километров')




