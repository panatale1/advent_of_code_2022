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

scenic_score = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        vertical = []
        for x in range(len(grid)):
            vertical.append(grid[x][j])
        left = grid[i][:j]
        left.reverse()
        right = grid[i][j + 1:]
        up = vertical[:i]
        up.reverse()
        down = vertical[i + 1:]
        left_score = 0
        for x in range(len(left)):
            if left[x] >= grid[i][j]:
                left_score = x + 1
                break
        else:
            left_score = len(left)
        right_score = 0
        for x in range(len(right)):
            if right[x] >= grid[i][j]:
                right_score = x + 1
                break
        else:
            right_score = len(right)
        up_score = 0
        for x in range(len(up)):
            if up[x] >= grid[i][j]:
                up_score = x + 1
                break
        else:
            up_score = len(up)
        down_score = 0
        for x in range(len(down)):
            if down[x] >= grid[i][j]:
                down_score = x + 1
                break
        else:
            down_score = len(down)
        if left_score * right_score * up_score * down_score > scenic_score:
            scenic_score = left_score * right_score * up_score * down_score
print(scenic_score)
        
