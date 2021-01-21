class Worker:
    my_dict = {'wage': 12000, 'bonus': 5000}
    name = 'Alex'
    surname = 'Tolubaev'
    position = 'Fitter'
    _income = my_dict


class Position(Worker):

    def get_full_name(self, name, surname):
        return name, surname

    def get_total_income(self):
        full_income = int(super()._income['wage'] + super()._income['bonus'])
        return full_income



a = Position()
input1 = 'Alex'
input2 = 'Tolubaev'
if Worker.name == input1 and Worker.surname == input2:
    b = a.get_full_name(name=input1, surname=input2)
    d = b[0] + ' ' + b[1]
    c = a.get_total_income()
    print(f'{d} {c} руб')
else:
    print('Нет такого сотрудника')
