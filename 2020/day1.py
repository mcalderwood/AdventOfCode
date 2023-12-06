import sys

with open('/Users/matt/Projects/Advent of Code/2020/aoc-day1-input.txt') as my_file:
    numbers_array = my_file.readlines()

for num1 in numbers_array:
    for num2 in numbers_array[1:]:
        for num3 in numbers_array[2:]:
            if int(num1) + int(num2) +int(num3) == 2020:
              print (int(num1) * int(num2) * int(num3))
              sys.exit()
