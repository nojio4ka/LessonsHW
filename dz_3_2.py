def func_1(**kwargs):
    return list(kwargs.values())


def func_2():
    print(func_1(name=input('Введите имя: '),
                surname=input('Введите фамилию: '),
                date=input('Введите дату рождения: '),
                town=input('Введите город: '),
                email=input('Введите почту: '),
                tel=input('Введите телефон: ')))

func_2()

