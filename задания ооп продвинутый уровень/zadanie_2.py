from abc import ABC, abstractmethod


class Clothes(ABC):
    pass


class PaymentSize(ABC):
    @abstractmethod
    def payment_size(self):
        pass


class PaymentHeight(ABC):
    @abstractmethod
    def payment_height(self):
        pass


class Coat(Clothes, PaymentSize):
    def __init__(self, size):
        self.size = size

    @property
    def payment_size(self):
        self.size = (self.size / 6.5 + 0.5)
        return self.size


class Costume(Clothes, PaymentHeight):
    def __init__(self, height):
        self.height = height

    @property
    def payment_height(self):
        self.height = (2 * self.height + 0.3)
        return self.height


a = Coat(40)
res_coat = a.payment_size
print(f'Для пальто нужно {round(res_coat,2)} ед ткани')

b = Costume(60)
res_costume = b.payment_height
print(f'Для костюма нужно {round(res_costume,2)} ед ткани')

res = round((res_costume + res_coat), 2)
print(f'Общий расход ткани {res} ед')
