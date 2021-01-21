class Road:
    length = 0
    width = 0

    def mass_calculation(self, lenght, width):
        self._lenght = lenght
        self._width = width
        result = lenght * width * 25 * 0.005
        return result

s = Road()
print(str(s.mass_calculation(5000, 20)) + ' т')