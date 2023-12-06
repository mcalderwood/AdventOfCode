import sys
import re
import numpy as np
from pathlib import Path
from scipy.signal import argrelmin

path = Path(__file__).parent / "aoc-day9-input-test.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

sizeX = 5
sizeY = 10
#sizeX = 100
#sizeY = 100
heightmap = np.ones(shape=(sizeX+2,sizeY+2), dtype=int) * 99

row = 1
for line in input_array:
    for i in range(sizeY):
        heightmap[row, i+1] = int(line[i])
    row += 1

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

print (sum)

#print(heightmap)