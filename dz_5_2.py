with open('test.txt', 'r') as abc:
    lines_n = 0
    words_n = 0
    for line in abc:
        lines_n += 1
        words = line.split()
        words_n += len(words)
    print(lines_n)
    print(words_n)
