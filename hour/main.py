sec = int(input('Сколько секнд желаете перевести в часы, минуты, секунды: '))
hour = sec // 3600
minuts = (sec // 60) % 60
second = sec % 60
print(f'{hour} чч {minuts} mm {second} cc')