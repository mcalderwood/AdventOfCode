import sys
from pathlib import Path

path = Path(__file__).parent / "aoc-day2-input.txt"
with open(path) as my_file:
    commands_array = my_file.readlines()

posX = 0
posY = 0
for command_str in commands_array:
    (command, amt) = command_str.split()
    if (command == 'forward'):
        posX += int(amt)
    elif (command == 'down'):
        posY += int(amt)
    elif (command == 'up'):
        posY -= int(amt)

print (posX * posY)