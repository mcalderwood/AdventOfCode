import sys
import re
import numpy as np
from pathlib import Path

path = Path(__file__).parent / "aoc-day9-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

sizeX = 100
sizeY = 100
heightmap = np.ones(shape=(sizeX+2,sizeY+2), dtype=int) * 99

def ExpandBasinSearch(heightmap, row, col):
    if heightmap[row,col] >= 9:
        return
    
    if (row, col) in basin_points:
        return

    basin_points.add((row,col))

    ExpandBasinSearch(heightmap, row-1, col)
    ExpandBasinSearch(heightmap, row+1, col)
    ExpandBasinSearch(heightmap, row, col-1)
    ExpandBasinSearch(heightmap, row, col+1)


row = 1
for line in input_array:
    for i in range(sizeY):
        heightmap[row, i+1] = int(line[i])
    row += 1

#print(heightmap)

low_points = []
sum = 0
for row in range(1, sizeX + 1):
    for col in range(1, sizeY + 1):
        above = heightmap[row-1,col]
        below = heightmap[row+1,col]
        left = heightmap[row,col-1]
        right = heightmap[row,col+1]
        val = heightmap[row,col]

        if val < above and val < below and val < left and val < right:
            sum += val + 1
            low_points.append((row, col))

basin_sizes = []
for row, col in low_points:
    basin_points = set()
    #basin_points.add((row,col))

    ExpandBasinSearch(heightmap, row, col)

    #print (len(basin_points))
    basin_sizes.append(len(basin_points))

    # Find adjacent non-9s
    # Add them to unique list of basin points
    #   Find their adjacent non-9s
    #       Recurse

basin_sizes.sort(reverse=True)
#print (basin_sizes[0], basin_sizes[1], basin_sizes[2])
print (basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
#print(heightmap)