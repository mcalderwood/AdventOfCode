import sys
import re
from pathlib import Path

path = Path(__file__).parent / "aoc-day8-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

numOf1478 = 0
for line in input_array:
    output = line.split('|')[1].strip().split(' ')
    for digit in output:
        l = len(digit)
        if l == 2 or l == 3 or l == 4 or l == 7:
            numOf1478 += 1

print (numOf1478)
