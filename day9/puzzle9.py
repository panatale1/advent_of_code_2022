from copy import deepcopy
from pprint import pprint

with open('input1', 'r') as input_data:
    directions = input_data.readlines()

tail_visited = [[0,0]]
head = [0,0]
tail = [0,0]
for line in directions:
    direction, distance = line.strip().split()
    distance = int(distance)
    for i in range(distance):
        if direction == 'R':
            head[0] += 1
            if head[1] - tail[1] == 0 and head[0] - tail[0] > 1: # same row, different columns
                tail[0] += 1
            elif head[1] - tail[1] != 0 and head[0] - tail[0] > 1:
                tail[0] += 1
                if head[1] - tail[1] > 0:
                    tail[1] += 1
                else:
                    tail[1] -= 1
        elif direction == 'L':
            head[0] -= 1
            if head[1] - tail[1] == 0 and head[0] - tail[0] < -1:
                tail[0] -= 1
            elif head[1] - tail[1] != 0 and head[0] - tail[0] < -1:
                tail[0] -= 1
                if head[1] - tail[1] > 0:
                    tail[1] += 1
                else:
                    tail[1] -= 1
        elif direction == 'U':
            head[1] += 1
            if head[0] - tail[0] == 0 and head[1] - tail[1] > 1:
                tail[1] += 1
            elif head[0] - tail[0] != 0 and head[1] - tail[1] > 1:
                tail[1] += 1
                if head[0] - tail[0] > 0:
                    tail[0] += 1
                else:
                    tail[0] -= 1
        elif direction == 'D':
            head[1] -= 1
            if head[0] - tail[0] == 0 and head[1] - tail[1] < -1:
                tail[1] -= 1
            elif head[0] - tail[0] != 0 and head[1] - tail[1] < -1:
                tail[1] -= 1
                if head[0] - tail[0] > 0:
                    tail[0] += 1
                else:
                    tail[0] -= 1
        if tail not in tail_visited:
            tail_visited.append(deepcopy(tail))
print(len(tail_visited))

def knot_moves(head, tail, direction):
    if direction == 'R':
        if head[1] - tail[1] == 0 and head[0] - tail[0] > 1:
            tail[0] += 1
        elif head[1] - tail[1] != 0 and head[0] - tail[0] > 1:
            tail[0] += 1
            if head[1] - tail[1] > 0:
                tail[1] += 1
            else:
                tail[1] -= 1
    elif direction == 'L':
        if head[1] - tail[1] == 0 and head[0] - tail[0] < -1:
            tail[0] -= 1
        elif head[1] - tail[1] != 0 and head[0] - tail[0] < -1:
            tail[0] -= 1
            if head[1] - tail[1] > 0:
                tail[1] += 1
            else:
                tail[1] -= 1
    elif direction == 'U':
        if head[0] - tail[0] == 0 and head[1] - tail[1] > 1:
            tail[1] += 1
        elif head[0] - tail[0] != 0 and head[1] - tail[1] > 1:
            tail[1] += 1
            if head[0] - tail[0] > 0:
                tail[0] += 1
            else:
                tail[0] -= 1
    elif direction == 'D':
        if head[0] - tail[0] == 0 and head[1] - tail[1] < -1:
            tail[1] -= 1
        elif head[0] - tail[0] != 0 and head[1] - tail[1] < -1:
            tail[1] -= 1
            if head[0] - tail[0] > 0:
                tail[0] += 1
            else:
                tail[0] -= 1
    
tail_visited = [[0,0]]
rope_dict = {i:[0,0] for i in range(10)}
for line in directions:
    direction, distance = line.strip().split()
    for i in range(int(distance)):
        if direction == 'R':
            rope_dict[0][0] += 1
        elif direction == 'L':
            rope_dict[0][0] -= 1
        elif direction == 'U':
            rope_dict[0][1] += 1
        elif direction == 'D':
            rope_dict[0][1] -= 1
        for j in range(1, 10):
            knot_moves(rope_dict[j-1], rope_dict[j], direction)
        if rope_dict[9] not in tail_visited:
            tail_visited.append(deepcopy(rope_dict[9]))
print(len(tail_visited))
