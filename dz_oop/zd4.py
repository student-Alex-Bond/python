import random


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police




    def go(self):
        print(f'Машина едет')

    def stop(self):
        print('Машина стоит')

    def turn(self):
        self.random_direction = random.randint(0, 1)
        if self.random_direction == 0:
            self.random_direction = 'налево'
            return 'Машина повернула ' + self.random_direction
        else:
            self.random_direction = 'направо'
            return 'Машина повернула ' + self.random_direction

    def show_speed(self, speed):
        return speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if self.speed > 60:
            return 'должна быть ниже 60 км/ч'
        else:
            return speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if self.speed > 40:
           return  'должна ниже 40 км\ч'
        else:
            return speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


a = WorkCar(39, 'Red', 'Грузовик', False)
b = SportCar(67, 'Gold', 'Cпортивная', False)
c = PoliceCar(107, 'Cтрогий', 'Полицейсая', True)
d= TownCar(64, 'Green', 'Трудяга', False)
for i in a, b, c, d:
    print(f'Тип машины: {i.name}')
    if i.speed > 0:
        i.go()
        print(f'Ee скорость {i.show_speed(i.speed)}')
        print(f'Цвет машины: {i.color}')

        if i.is_police == False:
            print('Машина не принадлежит полиции')
        else:
            print('Машина принадлежит полиции')
        print(i.turn())
    else:
        i.stop()
        print(f'Цвет машины: {i.color}')
        print(f'Тип машины: {i.name}')
        if i.is_police == False:
            print('Машина не принадлежит полиции')
        else:
            print('Машина принадлежит полиции')
    print()


