class Road():

    def __init__(self, _width, _length):
        self._width = _width
        self._length = _length

    def calc(self, density, depth):
        print(
            f'{self._width} м*{self._length} м* {density} кг* {depth} см = {self._width * self._length * density * depth} tons required')


tuymen_tobolsk = Road(20, 400000)
tuymen_tobolsk.calc(25, 5)
