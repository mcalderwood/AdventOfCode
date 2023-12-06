import re

with open('/Users/matt/Projects/Advent of Code/2020/aoc-day2-input.txt') as my_file:
    passwords_array = my_file.readlines()

valid_passwords = 0
for line in passwords_array:
    m = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    low = int(m.group(1))
    high = int(m.group(2))
    char = m.group(3)
    password = m.group(4)
    count = 0

    for x in password:
        if x == char:
            count += 1

    if count >= low and count <= high:
        valid_passwords += 1

print (valid_passwords)

