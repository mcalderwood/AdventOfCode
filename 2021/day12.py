#import sys
#import re
from queue import Queue
from pathlib import Path

def find_all_paths(caves, path, currentCave, goal):
    global paths
    #Q = Queue(maxsize=0)
    #explored = [root]
    new_path = path.copy()
    new_path.append(currentCave)

    if currentCave == goal:
        print (",".join(new_path))
        paths += 1
        return
    
    for adjacent_cave in caves[currentCave]:
        if (adjacent_cave.islower() and adjacent_cave not in path) or adjacent_cave.isupper():
            find_all_paths(caves, new_path, adjacent_cave, goal)


path = Path(__file__).parent / "aoc-day12-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

caves = {}
paths = 0

for line in input_array:
    (cave1, cave2) = line.strip(" \r\n").split('-')
    if cave1 not in caves:
        caves[cave1] = []
    if cave2 not in caves:
        caves[cave2] = []

    caves[cave1].append(cave2)
    caves[cave2].append(cave1)

find_all_paths(caves, [], "start", "end")

print(paths)