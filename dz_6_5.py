class Stationery:

    def __init__(self, title='Инструмент для рисования'):
        self.title = title

    def Draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):

    def Draw(self):
        print(f'Рисую с помощью- {self.title}')

class Pencil(Stationery):

    def Draw(self):
        print(f'Рисую с помощью- {self.title}')

class Handle(Stationery):

    def Draw(self):
        print(f'Рисую с помощью- {self.title}')

a = Stationery()
a.Draw()