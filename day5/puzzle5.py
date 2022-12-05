from string import ascii_uppercase
from pprint import pprint

read_stacks = []
directions = []
switch = False
with open('input1', 'r') as data:
    for line in data.readlines():
        if line != '\n':
            # not the separator line
            if switch:
                directions.append(line.strip().split())
            else:
                read_stacks.append(line)
        else:
            switch = True

indices = read_stacks.pop().split()
stacks = {}
for i in indices:
    stacks[i] = []
while read_stacks:
    start = 0
    index = 0
    row = read_stacks.pop()
    while start < len(row):
        for i in row[start:start+4]:
            if i in ascii_uppercase:
                stacks[indices[index]].append(i)
        start += 4
        index += 1

for line in directions:
    # used for part 1
    # for i in range(int(line[1])):
    #     stacks[line[5]].append(stacks[line[3]].pop())
    val = int(line[1]) * -1
    stacks[line[5]].extend(stacks[line[3]][val:])
    stacks[line[3]] = stacks[line[3]][:val]
result = ''
for k, v in stacks.items():
    result += v[-1]
print(result)
