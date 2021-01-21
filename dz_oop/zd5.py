class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки.'
class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки ручки'
class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки  карандаша.'
class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки маркера.'
a = Pen("Ручка")
print(a.title)
print(a.draw())
a = Pencil("Карандаш")
print(a.title)
print(a.draw())
a = Handle("Маркер")
print(a.title)
print(a.draw())
