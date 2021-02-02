class ComplexNumber:
    composition = str()
    res = str()
    list_complex_number = []

    def __init__(self, complex_number):
        self.complex_number = complex_number


    def __str__(self, res):
        self.res = res
        return self.res

    def transform_input(self, complex_number):
        tmp = complex_number
        tmp = ''.join(tmp.split())

        if tmp[len(tmp) - 1] != 'i':
            tmp = tmp + '+0i'
        global char
        char = tmp[len(tmp) - 1]
        tmp = tmp[:len(tmp) - 1]
        count = 0
        flag = False
        while flag == False:
            if tmp[(len(tmp) - 1) - count] == '-' or tmp[(len(tmp) - 1) - count] == '+':
                flag = True
            else:
                count += 1
        self.list_complex_number.append(tmp[:len(tmp) - count - 1])
        self.list_complex_number.append(tmp[len(tmp) - count - 1:len(tmp)])

        return self.list_complex_number

    def __add__(self, other):
        self.transform_input(self.complex_number)
        self.transform_input(other.complex_number)
        res = ''
        list = []
        for i in range(len(self.list_complex_number)//2):
            a = int(self.list_complex_number[i]) + int(self.list_complex_number[i+2])
            list.append(a)
        if list[1] == 0:
            self.res = list[0]
        elif list[1] < 0:
            self.res = str(list[0]) + ' ' + str(list[1]) + char
        else:
            self.res = str(list[0]) + '+' + str(list[1]) + char
        return self.res

    def __mul__(self, other):
        self.transform_input(self.complex_number)
        self.transform_input(other.complex_number)
        composition = ''
        list = []
        list.clear()
        a = int(self.list_complex_number[0]) * int(self.list_complex_number[2])
        b = int(self.list_complex_number[0]) * int(self.list_complex_number[3])
        c = int(self.list_complex_number[1]) * int(self.list_complex_number[2])
        d = int(self.list_complex_number[1]) * int(self.list_complex_number[3]) * (-1)
        e = a + (-d)  # 1
        f = (-b) + c  # 2
        if int(f) < 0:
            self.res = str(e) + ' ' + str(f) + char
        else:
            self.res = str(e) + '+' + str(f) + char

        return self.res


complex_number_1 ='122+678i'  #input('Введите первое комплексное число: ')
complex_number_2 ='156-567i' #input('Введите второе комплексное число: ')

exp_1 = ComplexNumber(complex_number_1)
exp_2 = ComplexNumber(complex_number_2)


summa = (exp_1 + exp_2)
print(f'Результат сложения: {summa}')
comp = (exp_1 * exp_2)
print(f'Результат умножения: {comp}')