def my_func():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    if b != 0:
        result = a / b
        print(result)
    else:
        print('Деление на ноль невозможно')
    return

my_func()
