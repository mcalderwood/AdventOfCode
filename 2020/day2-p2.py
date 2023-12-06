import re

with open('/Users/matt/Projects/Advent of Code/2020/aoc-day2-input.txt') as my_file:
    passwords_array = my_file.readlines()

valid_passwords = 0
for line in passwords_array:
    m = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    pos1 = int(m.group(1))
    pos2 = int(m.group(2))
    char = m.group(3)
    password = m.group(4)
    count = 0

    try:
        if password[pos1-1] == char:
            count += 1
    
        if password[pos2-1] == char:
            count += 1
    except IndexError:
        print(pos1, pos2, password)

    if count == 1:
        valid_passwords += 1

print (valid_passwords)

