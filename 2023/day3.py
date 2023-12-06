from pathlib import Path
import numpy as np

def get_next_number(line, startIndex):
    start = startIndex
    while start < len(line) and (line[start] < '0' or line[start] > '9'):
        start += 1

    if start >= len(line):
        return (-1, -1, -1)
    
    end = start + 1
    while end < len(line) and line[end] >= '0' and line[end] <= '9':
        end += 1

    return (start, end - 1, line[start:end])
    


path = Path(__file__).parent / "aoc-day3-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

rowLength = len(lines)
colLength = len(lines[0])

schematic = np.zeros((rowLength + 2, colLength + 2), dtype='int8')

part_numbers = 0

row = 1
for line in lines:
    for i in range(len(line.strip())):
        if line[i] != '.' and (line[i] < '0' or line[i] > '9'):
            schematic[row, i+1] = 1
    row += 1

row = 1
for line in lines:
    x = 0
    while x < len(line):
        begin, end, number = get_next_number(line, x)
        if begin == -1:
            break
        
        add = False
        for i in range(row - 1, row + 2):
            for j in range(begin, end + 3):
                if schematic[i, j] == 1:
                    add = True
        
        if add == True:
            part_numbers += int(number)
        
        x = end + 2
    row += 1


print(part_numbers)
        