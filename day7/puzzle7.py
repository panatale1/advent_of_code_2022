from flexdict import FlexDict
from copy import deepcopy
from pprint import pprint

terminal = []
with open('input1', 'r') as input_data:
    for line in input_data.readlines():
        terminal.append(line.strip())

dir_tree = ['total']
totals = FlexDict()
totals['/', 'total'] = 0
print(totals)

for i in terminal:
    # 3 different options
    if i.startswith('$'):
        # command input
        if i.split()[1] == 'cd':
            # change directory
            if i.split()[2] == '..':
                # back up a level
                total = totals[dir_tree]
                dir_tree.pop(-2)
                totals[dir_tree] += total
            else:
                dir_tree.insert(-1,i.split()[2])
        elif i.split()[1] == 'ls':
            # lists directory contents
            pass
    elif i.startswith('dir'):
        # ls output for directory
        dirtree = deepcopy(dir_tree)
        dirtree.insert(-1,i.split()[1])
        totals[dirtree] = 0
    elif int(i.split()[0]):
        #ls output for file
        totals[dir_tree] += int(i.split()[0])
while len(dir_tree) > 2:
    total = totals[dir_tree]
    dir_tree.pop(-2)
    totals[dir_tree] += total
total_list = totals.values(nested=True)
print(sum([i for i in total_list if i <= 100000]))

used_filespace = totals['/', 'total']
total_filespace = 70000000
required_filespace = 30000000
free_filespace = total_filespace - used_filespace
big_dirs = []
for i in total_list:
    if free_filespace + i >= required_filespace:
        big_dirs.append(i)
big_dirs.sort()
print(big_dirs[0])
