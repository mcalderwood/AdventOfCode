import sys
from pathlib import Path

path = Path(__file__).parent / "aoc-day3-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

bit_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
input_size = len(input_array)

for num in input_array:
    for i in range(0,12):
        if num[i] == '1':
            bit_counts[i] += 1

gamma = 0
epsilon = 0

for i in range(0,12):
    if bit_counts[i] > input_size / 2:
        gamma += 1 << (11 - i)
    else:
        epsilon += 1 << (11 - i)

print (gamma)
print (epsilon)
print (gamma * epsilon)