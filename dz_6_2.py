class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return f'{self._length} м * {self._width} м * 25кг * 5см = {(self._length * self._width * 25 * 5) / 1000} т'

road_m = Road(20, 100)
print(road_m.mass())
