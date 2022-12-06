with open('input1', 'r') as input_data:
    lines = input_data.readlines()

signal = lines[0].strip()

found = False
index = 0

for i in range(len(signal)):
    for j in range(4):
        if signal[i:i+4].count(signal[i:i+4][j]) > 1:
            # Definitely not the marker
            break
    else:
        found = True
        index = i + 4
    if found:
        break
print(index)

found = False
index = 0

for i in range(len(signal)):
    for j in range(14):
        if signal[i:i+14].count(signal[i:i+14][j]) > 1:
            # Definitely not the marker
            break
    else:
        found = True
        index = i + 14
    if found:
        break
print(index)
