#import sys
#import re
import numpy as np
from pathlib import Path

path = Path(__file__).parent / "aoc-day11-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

size = 10
numSteps = 500
octopi = np.zeros((size,size), dtype=int)

row = 0
for line in input_array:
    col = 0
    for c in line:
        if c != '\r' and c != '\n':
            octopi[row,col] = int(c)
        col += 1
    row += 1 

for step in range(1,numSteps):
    octopi += 1
    octopi_pad = np.pad(octopi, (1,), 'constant', constant_values=(-200))
    
    while np.any(octopi_pad > 9):
        for row in range(1,size+1):
            for col in range(1,size+1):
                if octopi_pad[row,col] > 9:
                    octopi_pad[row-1:row+2,col-1:col+2] += 1
                    octopi_pad[row,col] = -200
    
    octopi = np.maximum(octopi_pad, [0])[1:size+1,1:size+1]

    if np.all(octopi == 0):
        break

print(step)