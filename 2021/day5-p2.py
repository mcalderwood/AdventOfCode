import sys
import re
from pathlib import Path

path = Path(__file__).parent / "aoc-day5-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

# Create 1000x1000 array
vents = [ [0] * 1000 for i in range(1000)]

for line in input_array:
    m = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line)
    x1 = int(m.group(1))
    y1 = int(m.group(2))
    x2 = int(m.group(3))
    y2 = int(m.group(4))

    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            vents[x1][y] += 1
    elif y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            vents[x][y1] += 1
    else:
        x = x1
        y = y1
        while x != x2 and y != y2:
            vents[x][y] += 1
            if x2 > x1:
                x += 1
            else:
                x -= 1
            if y2 > y1:
                y += 1
            else:
                y -= 1
        vents[x][y] += 1


count = 0
for y in range(1000):
    for x in range(1000):
        print (vents[x][y], end='')
        if vents[x][y] >= 2:
            count += 1
    print()
print(count)