from pathlib import Path
from math import lcm
import re

path = Path(__file__).parent / "aoc-day8-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

class Node:
    def __init__(self, location, left, right):
        self.location = location
        self.left = left
        self.right = right

def final_state_met(current_locations):
    for location in current_locations:
        if location[2] != 'Z':
            return False
    return True

all_instructions = lines[0].strip()

nodes = {}

for line in lines[2:]:
    m = re.match(r"^(\w{3}) = \((\w{3}), (\w{3})\)$", line.strip())
    new_location = m.group(1)
    left = m.group(2)
    right = m.group(3)

    nodes[new_location] = Node(new_location, left, right)

current_locations = []
steps = 0

print(lcm(11567, 12643, 14257, 16409, 19099, 21251))

# find all locations ending in A, put in current_locations
for node in nodes:
    if nodes[node].location[2] == 'A':
        current_locations.append(nodes[node].location)

while not final_state_met(current_locations):
    current_instruction = all_instructions[steps % len(all_instructions)]
    steps += 1
    zs = 0
    for i in range(len(current_locations)):
        if current_instruction == 'L':
            current_locations[i] = nodes[current_locations[i]].left
        else:
            current_locations[i] = nodes[current_locations[i]].right
        if current_locations[i][2] == 'Z':
            print(steps, i, current_locations[i])
    #if zs >= 3:
        #print(current_locations, zs, steps)

print(steps)