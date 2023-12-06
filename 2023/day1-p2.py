import sys
from pathlib import Path

path = Path(__file__).parent / "aoc-day1-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

valid_digits = ["zero", "0",
    "one", "1",
    "two", "2",
    "three", "3",
    "four", "4",
    "five", "5",
    "six", "6",
    "seven", "7",
    "eight", "8",
    "nine", "9"]

def get_value(str):
    return valid_digits.index(str) // 2

numbers = []

for line in lines:
#line = lines[3]
    first_digit_pos = len(line)
    first_digit = ''
    last_digit_pos = len(line)
    last_digit = ''

    reversed_line = line[::-1]

    for digit in valid_digits:
        pos = line.find(digit)
        if pos >= 0 and pos < first_digit_pos:
            first_digit_pos = pos
            first_digit = digit

        pos = reversed_line.find(digit[::-1])
        if pos >= 0 and pos < last_digit_pos:
            last_digit_pos = pos
            last_digit = digit

    numbers.append((get_value(first_digit) * 10) + get_value(last_digit))

print(sum(numbers))

