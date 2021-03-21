def sum ():
    sum_res = 0
    exit_func = False
    while exit_func == False:
        number = input('Введите числа через пробел, для выхода введите Q ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                exit_func = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма чисел равна {sum_res}')



sum()
