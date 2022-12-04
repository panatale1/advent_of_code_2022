with open('input1', 'r') as input_data:
    pairs = input_data.readlines()
for i in range(len(pairs)):
    pairs[i] = pairs[i].strip().split(',')

counter = 0
for pair in pairs:
    first = pair[0].split('-')
    second = pair[1].split('-')
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
        # second contained within first
        counter += 1
    elif int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1]):
        # first contained within second
        counter += 1
print(counter)

counter = 0
for pair in pairs:
    first = [i for i in range (int(pair[0].split('-')[0]), int(pair[0].split('-')[1]) + 1)]
    second = [i for i in range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1]) + 1)]
    for i in first:
        if i in second:
            counter += 1
            break
print(counter)
