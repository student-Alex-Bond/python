num = int(input('Введите целое число:'))
max = 0
while num > 0:
    b = num % 10
    num = num // 10
    if b >= max:
        max = b

print(max)
