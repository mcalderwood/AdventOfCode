import sys
from pathlib import Path

path = Path(__file__).parent / "aoc-day1-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

numbers = []

for line in lines:
#line = lines[1]
    for char in line:
        if char >= '0' and char <= '9':
            first_digit = int(char)
            break

    for char in reversed(line):
        if char >= '0' and char <= '9':
            last_digit = int(char)
            break

    numbers.append((first_digit * 10) + last_digit)

print(sum(numbers))

