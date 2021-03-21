class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'New car: {self.name} (color {self.color}) car is a police - {self.is_police}')

    def go(self):
        print(f'{self.name} started')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} Car turn right' if direction == rigth else 'Car turn left')

    def show_speed(self):
        print(f'Current speed {self.name} is {self.speed}')


class WorkCar(Car):

        def show_speed(self):
           return f'{self.name}: Speed like {self.speed} is HIGH Speed' \
            if self.speed > 40 else f'{self.name}: speed is {self.speed}'


class SportCar(Car):
    """Sport Car"""

class PoliceCar(Car):

        def __init__(self, speed, color, name, is_police=True):
            super().__init__(speed, color, name, is_police)


sheriff_car = PoliceCar(100, 'black', 'Sheriff')
sheriff_car.go()
