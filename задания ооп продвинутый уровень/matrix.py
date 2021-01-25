class Matrix:
    new_list = []
    my_str = ''

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.new_list.clear()
        for i in self.matrix:
            for j in range(len(i)):
                self.new_list.append(str(i[j]))
                self.new_list.append(' ')
            self.new_list.append('\n')
        self.my_str = ''.join(self.new_list)
        return f'{self.my_str}'

    def __add__(self, other):
        self.new_list.clear()

        for i, j in zip(self.matrix, other.matrix):
            for k in range(len(i)):
                term_1 = int(i[k])
                term_2 = int(j[k])
                summa = term_1 + term_2
                self.new_list.append(str(summa))
                self.new_list.append(' ')
            self.new_list.append('\n')
        self.my_str = ''.join(self.new_list)
        return f'{self.my_str}'


matrix_1 = Matrix([[10, -2, 3], [4, 5, 8], [-7, 8, 9]])
print('matrix_1')
print(matrix_1)

matrix_2 = Matrix([[9, 88, 7], [6, -5, 4], [3, -2, 1]])
print('matrix_2')
print(matrix_2)

matrix_summa = (matrix_1 + matrix_2)
print('matrix_summa')
print(matrix_summa)
