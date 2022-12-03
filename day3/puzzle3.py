from string import ascii_lowercase, ascii_uppercase

with open('input1', 'r') as input_data:
    sacks = input_data.readlines()
for i in range(len(sacks)):
    sacks[i] = sacks[i].strip()

ascii_letters = ascii_lowercase + ascii_uppercase
priorities = {ascii_letters[i]: i + 1 for i in range(len(ascii_letters))}

priority_val = 0
for line in sacks:
    half = int(len(line)/2)
    comp_1 = line[:half]
    comp_2 = line[half:]
    for i in comp_1:
        if i in comp_2:
            priority_val += priorities[i]
            break
print(priority_val)

priority_val = 0
start = 0
while start < len(sacks):
    group = sacks[start:start + 3]
    for i in group[0]:
        if i in group[1] and i in group[2]:
            priority_val += priorities[i]
            break
    start += 3
print(priority_val)
