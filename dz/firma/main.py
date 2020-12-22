proceeds = float(input('Введите выручку вашей фирмы: '))
cost = float(input('Введите издержки вашей фирмы:'))
if proceeds > cost:
    print('Ваша фирма отработала с прибылью.')
    profit = proceeds - cost
    rent = (profit / proceeds) * 100
    print('Рентабельность вашей фирмы: '+ str(int(rent))+ ' %')
    amount = float(input('Сколько сотрудников в ващей фирме: '))
    worker = profit / amount
    print(f'Прибыль на одного сотрудника составила {worker:.2f} ед')
else:
    print('Ваша фирма работает в убыток.')
