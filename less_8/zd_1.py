class Data:

    def __init__(self, my_str):
        self.my_str = my_str

    @classmethod
    def transform_my_str(cls, my_str):
        cls.my_str_1 = [int(i) for i in my_str]
        data_list = cls.my_str_1
        return data_list

    @staticmethod
    def valid_my_str():
        data_str = ''
        a = Data.transform_my_str(my_str)
        if 0 < a[0] > 32:
            data_str = data_str + 'Неверная дата'+'\n'
        if 0 < a[1] > 13:
            data_str = data_str +'Неверный месяц' + '\n'
        if -7001 < a[2] > 2022:
            data_str = data_str + 'Неверный год'
        if len(data_str) > 0:
            return data_str
        else:
            return f'Дата введена верно'


my_str = input('Введите дату в формате день-месяц-год: ').split('-')
a = Data(my_str)
b = Data.valid_my_str()
print(b)
