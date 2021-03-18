with open('test.txt', 'w') as my_file:
    line = input('Введите текст: ')
    while line:
        my_file.write(f'{line}\n')
        line = input('Введите текст: ')
        if not line:
            break






