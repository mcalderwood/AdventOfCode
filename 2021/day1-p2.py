import sys
from pathlib import Path

path = Path(__file__).parent / "aoc-day1-input.txt"
with open(path) as my_file:
    numbers_array = my_file.readlines()

num_increases = 0
prev_num = int(numbers_array[0]) + int(numbers_array[1]) + int(numbers_array[2])
for i in range(3,len(numbers_array)):
    # print ("Compare " + str(prev_num) + " to " + num1)

    #if prev_num == -1:
    #    prev_num = int(num1)
    #    continue
    new_sum = int(numbers_array[i]) + int(numbers_array[i-1]) + int(numbers_array[i-2])
    if new_sum > prev_num:
        num_increases += 1
    prev_num = new_sum

print (num_increases)