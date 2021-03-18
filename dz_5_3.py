with open('test.txt', 'r') as f:
    a = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'{round(sum(a.values()) / len(a), 3)}\n'
          f'{[e[0] for e in a.items() if e[1] < 20000]}')