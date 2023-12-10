from pathlib import Path
import re

path = Path(__file__).parent / "aoc-day8-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

class Node:
    def __init__(self, location, left, right):
        self.location = location
        self.left = left
        self.right = right

all_instructions = lines[0].strip()

nodes = {}

for line in lines[2:]:
    m = re.match(r"^(\w{3}) = \((\w{3}), (\w{3})\)$", line.strip())
    new_location = m.group(1)
    left = m.group(2)
    right = m.group(3)

    nodes[new_location] = Node(new_location, left, right)

current_location = "AAA"
steps = 0
while current_location != "ZZZ":
    current_instruction = all_instructions[steps % len(all_instructions)]
    steps += 1
    if current_instruction == 'L':
        current_location = nodes[current_location].left
    else:
        current_location = nodes[current_location].right

print(steps)