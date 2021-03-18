import json

with open('7.json', 'w') as a:
    with open('7.txt') as b:
        profit = {name.split()[0]: int(name.split()[2]) - int(name.split()[3]) for name in b}
        result = [profit, {'Средняя прибыль: ': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                      len([int(i) for i in profit.values() if int(i) > 0]))}]

    json.dump(result, a, ensure_ascii=False, indent=4)