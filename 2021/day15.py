from pathlib import Path

path = Path(__file__).parent / "aoc-day15-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

size = 100
map = []

for line in input_array:
    new_line = []
    for c in line.strip(" \r\n"):
        new_line.append(int(c))
    map.append(new_line)
map[0][0] = 0

for y in reversed(range(len(map))):
    for x in reversed(range(len(map[y]))):
        options = []        
        if y < len(map) - 1:
            options.append(map[y+1][x])
        if x < len(map[y]) - 1:
            options.append(map[y][x+1])
        if len(options) > 0:
            map[y][x] += min(options)

print (map[0][0])