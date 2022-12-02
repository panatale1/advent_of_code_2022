with open('input1', 'r') as input_data:
    data = input_data.readlines()

total = 0
elf_totals = []
for i in data:
    try:
        total += int(i)
    except ValueError:
        elf_totals.append(total)
        total = 0

max_cals = max(elf_totals)
print(max_cals)

elf_totals.sort()
total = 0
for i in elf_totals[-3:]:
    print(i)
    total += i
print(total)
