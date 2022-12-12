from pprint import pprint
from math import floor, prod

with open('input1', 'r') as input_data:
#with open('test.txt', 'r') as input_data:
    monkey_data = input_data.readlines()

monkeys = {}
monkey = []
count = 0
for line in monkey_data:
    if line != '\n':
        monkey.append(line.strip())
    else:
        items = monkey[1].split(':')[1].strip().split(', ')
        monkeys[count] = {}
        monkeys[count]['items'] = []
        for item in items:
            monkeys[count]['items'].append(int(item))
        monkeys[count]['test'] = int(monkey[3].strip().split()[-1])
        monkeys[count]['operation'] = monkey[2].strip().split(':')[1].strip().split('=')[-1].strip()
        monkeys[count][True] = int(monkey[4].strip().split()[-1])
        monkeys[count][False] = int(monkey[5].strip().split()[-1])
        monkeys[count]['total_items'] = 0
        monkey = []
        count += 1
else:
    items = monkey[1].split(':')[1].strip().split(', ')
    monkeys[count] = {}
    monkeys[count]['items'] = []
    for item in items:
        monkeys[count]['items'].append(int(item))
    monkeys[count]['test'] = int(monkey[3].strip().split()[-1])
    monkeys[count]['operation'] = monkey[2].strip().split(':')[1].strip().split('=')[-1].strip()
    monkeys[count][True] = int(monkey[4].strip().split()[-1])
    monkeys[count][False] = int(monkey[5].strip().split()[-1])
    monkeys[count]['total_items'] = 0

mod = prod([monkeys[key]['test'] for key in monkeys.keys()])
for i in range(10000):
    keys = list(monkeys.keys())
    keys.sort()
    for key in keys:
        while len(monkeys[key]['items']) > 0:
            old = monkeys[key]['items'].pop(0)
            #new = floor(eval(monkeys[key]['operation']) / 3)
            new = eval(monkeys[key]['operation']) % mod
            if new % monkeys[key]['test'] == 0:
                monkeys[monkeys[key][True]]['items'].append(new)
            else:
                monkeys[monkeys[key][False]]['items'].append(new)
            monkeys[key]['total_items'] += 1

totals = [monkeys[key]['total_items'] for key in monkeys.keys()]
totals.sort()
print(totals[-1] * totals[-2])
