class Store:
    total_equipment = {'printer': 70, 'scanner': 70, 'copier': 70}
    balance_equipment = {'printer': 70, 'scanner': 70, 'copier': 70}
    number_in_subdivisions = {'bookkeeping': {'printer': 0, 'scanner': 0, 'copier': 0},
                              'personnel_department': {'printer': 0, 'scanner': 0, 'copier': 0},
                              'production': {'printer': 0, 'scanner': 0, 'copier': 0}}
    tmp = []

    def add_of_store(self):
        tmp = self
        for key, value in Store.total_equipment.items():
            if key == tmp[0]:
                Store.total_equipment[key] = tmp[1] + value
                Store.balance_equipment[key] = tmp[1] + value
        return Store.total_equipment

    def transfer_to_subdivision(self):
        tmp = self
        for key, value in Store.number_in_subdivisions.items():
            if key == tmp[0]:
                Store.number_in_subdivisions[key][tmp[1]] = value[tmp[1]] + tmp[2]

        for key, value in Store.balance_equipment.items():
            if key == tmp[1]:
                Store.balance_equipment[tmp[1]] = value - tmp[2]
        return Store.number_in_subdivisions

    @staticmethod
    def output_total_equiement():
        return f'Всего оргтехники на складе: {Store.total_equipment}'

    @staticmethod
    def output_number_in_subdivisions():
        return f'Всего оргтехники в подразделениях: {Store.number_in_subdivisions}'

    @staticmethod
    def output_balance_equipment():
        return f'Остаток оргтехники на складе: {Store.balance_equipment}'


class OfficeEquipment:
    information = 'Передача информации на вывод или ввод'
    papier = 'Эти устройства работают с бумажными носителями'


class Printer(OfficeEquipment):

    my_print = 'Выводит информацию на бумажный носитель'


class Scanner(OfficeEquipment):

    scan = 'Принимает на вход информацию с бумажных носителей '


class Copier(OfficeEquipment):

    copier = 'Делает копию бумажного носителя'






print('1 - добавить оргтехнику на склад')
print('2 - для передачи техники в подразделения')
print('3 - просмотеть общее количество оргтехники на складе')
print('4 - просмотреть остаток оргтехники на складе')
print('5 - просмотреть сколько огртехники в подразделениях')
print('0 - для выхода')
flag = True
while flag == True:
    print('Выберите действие: ')
    inp_data = input('--->')
    if inp_data == '0':
        flag = False
        break
    elif inp_data == '1':
        a = ''
        for key in Store.total_equipment.keys():
            a = a + str(key) + ' '
        print(f'Тип оргтехники: {a}')
        inp_data = input('Введите тип оргтехники и количество через пробел: ')
        tmp = inp_data.split(' ')
        if tmp[0].isdigit():
            print('Введите корректно данные')
        else:
            tmp[1] = int(tmp[1])
            Store.add_of_store(tmp)
    elif inp_data == '2':
        a = ''
        for key in Store.number_in_subdivisions.keys():
            a = a + str(key) + ' '
        print(f'Подразделения: {a}')
        a =''
        for key in Store.total_equipment.keys():
            a = a + str(key) + ' '
        print(f'Тип оргтехники: {a}')
        inp_data = input('Введите подразделение, тип оргтехники, количество через пробел: ')
        tmp = inp_data.split(' ')
        if tmp[0].isdigit() and tmp[1].isdigit():
            print('Введите корректно данные')
        else:
            tmp[2] = int(tmp[2])
            Store.transfer_to_subdivision(tmp)
    elif inp_data == '3':
        print(Store.output_total_equiement())

    elif inp_data == '4':
        print(Store.output_balance_equipment())

    elif inp_data == '5':
        print(Store.output_number_in_subdivisions())
