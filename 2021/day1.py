import sys
from pathlib import Path

path = Path(__file__).parent / "aoc-day1-input.txt"
with open(path) as my_file:
    numbers_array = my_file.readlines()

num_increases = 0
prev_num = -1
for num1 in numbers_array:
    print ("Compare " + str(prev_num) + " to " + num1)
    if prev_num == -1:
        prev_num = int(num1)
        continue
    if int(num1) > prev_num:
        num_increases += 1
    prev_num = int(num1)

print (num_increases)