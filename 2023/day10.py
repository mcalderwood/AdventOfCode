from pathlib import Path
import numpy as np

path = Path(__file__).parent / "aoc-day10-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

def are_connected_vertical(pos_above, pos_below):
    pipe_above = pipe_map[pos_above[0], pos_above[1]]
    pipe_below = pipe_map[pos_below[0], pos_below[1]]

    if (pipe_above == 'S' or pipe_above == '|' or pipe_above == '7' or pipe_above == 'F') and (pipe_below == 'S' or pipe_below == '|' or pipe_below == 'L' or pipe_below == 'J'):
        return True
    else:
        return False

def are_connected_horizontal(pos_left, pos_right):
    pipe_left = pipe_map[pos_left[0], pos_left[1]]
    pipe_right = pipe_map[pos_right[0], pos_right[1]]

    if (pipe_left == 'S' or pipe_left == '-' or pipe_left == 'L' or pipe_left == 'F') and (pipe_right == 'S' or pipe_right == '-' or pipe_right == 'J' or pipe_right == '7'):
        return True
    else:
        return False

def find_connected_positions(pos):
    connected_positions = []
    #current_pipe = pipe_map[pos[0], pos[1]]

    pipe_above_pos = (pos[0] - 1, pos[1])
    pipe_below_pos = (pos[0] + 1, pos[1])
    pipe_left_pos = (pos[0], pos[1] - 1)
    pipe_right_pos = (pos[0], pos[1] + 1)

    #pipe_above = pipe_map[pipe_above_pos[0], pipe_above_pos[1]]
    #pipe_below = pipe_map[pipe_below_pos[0], pipe_above_pos[1]]
    #pipe_left = pipe_map[pip_pos[0], pipe_above_pos[1]]
    #pipe_right = pipe_map[pipe_above_pos[0], pipe_above_pos[1]]

    if are_connected_vertical(pipe_above_pos, pos):
        connected_positions.append(pipe_above_pos)
    
    if are_connected_vertical(pos, pipe_below_pos):
        connected_positions.append(pipe_below_pos)

    if are_connected_horizontal(pipe_left_pos, pos):
        connected_positions.append(pipe_left_pos)

    if are_connected_horizontal(pos, pipe_right_pos):
        connected_positions.append(pipe_right_pos)

    return connected_positions

column_size = len(lines[0].strip()) + 2
row_size = len(lines) + 2

pipe_map = np.zeros((row_size, column_size), dtype='<U1')

for row in range(len(lines)):
    for col in range(len(lines[row])):
        pipe_map[row+1, col+1] = lines[row][col]

# Find 'S' position
posS = (-1, -1)
for row in range(len(lines)):
    col = lines[row].find('S')
    if col != -1:
        posS = (row+1, col+1)
        break

# Find two paths from S
next_positions = find_connected_positions(posS)
path_1_position = next_positions[0]
path_2_position = next_positions[1]
path_1_position_last = path_2_position_last = posS

steps = 1

#print("Path 1 position: ", path_1_position)
#print("Path 2 position: ", path_2_position)

# Move along paths until they converge at the same position
while path_1_position != path_2_position:
    next_positions = find_connected_positions(path_1_position)
    
    if next_positions[0] == path_1_position_last:
        path_1_position_last = path_1_position
        path_1_position = next_positions[1]
    else:
        path_1_position_last = path_1_position
        path_1_position = next_positions[0]

    next_positions = find_connected_positions(path_2_position)
    
    if next_positions[0] == path_2_position_last:
        path_2_position_last = path_2_position
        path_2_position = next_positions[1]
    else:
        path_2_position_last = path_2_position
        path_2_position = next_positions[0]

    #print("Path 1 position: ", path_1_position)
    #print("Path 2 position: ", path_2_position)
    steps += 1

print(steps)