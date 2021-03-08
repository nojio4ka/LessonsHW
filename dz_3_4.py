def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


print(my_func(float(input("Введите первое число: ")), int(input("Введите второе число"))))