from pprint import pprint

with open('input1', 'r') as input_data:
    commands = input_data.readlines()

X = 1
cycle = 0
interesting_cycles = [20, 60, 100, 140, 180, 220]
signal_strengths = 0
screen = [[' ' for i in range(40)] for j in range(6)]

for line in commands:
    command = line.strip()
    if command == 'noop':
        if cycle % 40 in [X - 1, X, X + 1]:
            row = int(cycle/40)
            index = cycle % 40
            screen[row][index] = '#'
        cycle += 1
        if cycle in interesting_cycles:
            signal_strengths += X * cycle
    else:
        reg = int(command.split()[1])
        for i in range(2):
            if cycle % 40 in [X - 1, X, X + 1]:
                row = int(cycle/40)
                index = cycle % 40
                screen[row][index] = '#'
            cycle += 1
            if cycle in interesting_cycles:
                signal_strengths += X * cycle
        else:
            X += reg
print(signal_strengths)

for i in screen:
    print(''.join(i))
