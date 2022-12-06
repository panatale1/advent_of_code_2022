def find_marker(signal, marker_len):
    found = False
    index = 0
    for i in range(len(signal)):
        for j in range(marker_len):
            if signal[i:i + marker_len].count(signal[i:i + marker_len][j]) > 1:
                break
        else:
            found = True
            index = i + marker_len
        if found:
            break
    print(index)

with open('input1', 'r') as input_data:
    lines = input_data.readlines()

signal = lines[0].strip()

find_marker(signal, 4)
find_marker(signal, 14)
