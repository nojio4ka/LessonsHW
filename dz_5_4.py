rus_dict = {'One': 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
with open('4r.txt', 'w') as a, open('4e.txt', 'r') as b:
    a.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in b]))