import sys
import re
from pathlib import Path

path = Path(__file__).parent / "aoc-day6-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

fish = []

for f in input_array[0].split(","):
    fish.append(int(f))

for day in range(80):
    num_fish_to_add = 0
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            num_fish_to_add += 1
        else:
            fish[i] -= 1
    for j in range(num_fish_to_add):
        fish.append(8)

print (len(fish))
