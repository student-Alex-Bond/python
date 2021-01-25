class Cell:
    my_str = ''
    def __init__(self, number_cells):
        self.number_cells = number_cells

    def __str__(self):
        return f'{self.number_cells}'

    def __add__(self, other):
        return Cell(self.number_cells + other.number_cells)

    def __sub__(self, other):
        if (self.number_cells - other.number_cells) > 0:
            return Cell(self.number_cells - other.number_cells)
        else:
            return f'Общее количество клеток меньше 0'

    def __mul__(self, other):
        return Cell(self.number_cells * other.number_cells)

    def __floordiv__(self, other):
        return Cell(round(self.number_cells // other.number_cells))

    def __call__(self, *args, **kwargs):
        return self.number_cells

    def make_order(self, *args, cells_in_row):
        a = args[0]
        a = round(a.number_cells)
        b = cells_in_row
        count = 0
        c = b
        for i in range(a):
            if count == c - 1:
                self.my_str = self.my_str + '*'
                self.my_str = self.my_str + '\n'
                c = c + b
                count += 1
            else:
                self.my_str = self.my_str + '*'
                count += 1
        return f'{self.my_str}'

cell_1 = Cell(2.8)
cell_2 = Cell(3.7)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print()
print('Метод make_order для cell_1')
print(cell_1.make_order(cell_1, cells_in_row=3))
print()
print('Метод make_order для cell_2')
print(cell_2.make_order(cell_2, cells_in_row=3))