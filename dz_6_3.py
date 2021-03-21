class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

        def get_full_name(self):
            return f'{self.name} {self.surname}'
        def get_total_income(self):
            return f'{sum(self._income.values())}'

a = Position('John', 'Jordan', 'Manager', 20000, 5000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

