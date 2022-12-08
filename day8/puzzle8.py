grid = []
with open('input1', 'r') as input_data:
    lines = input_data.readlines()

for line in lines:
    newline = []
    line = line.strip()
    for j in line:
        newline.append(int(j))
    grid.append(newline)

visible_trees = 0
print(grid[0])
visible_trees += len(grid[0])
visible_trees += len(grid[-1])
visible_trees += 2 * len(grid[1:-1])
print(visible_trees)

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        vertical = []
        for x in range(len(grid)):
            vertical.append(grid[x][j])
        left = grid[i][:j]
        right = grid[i][j + 1:]
        up = vertical[:i]
        down = vertical[i + 1:]
        if grid[i][j] > max(left) or grid[i][j] > max(right) or grid[i][j] > max(up) or grid[i][j] > max(down):
            visible_trees += 1
print(visible_trees)
