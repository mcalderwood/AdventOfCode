import sys
import re
from pathlib import Path

def fuel_usage(crabs, x):
    sum = 0
    for c in crabs:
        sum += abs(c - x)
    return sum

path = Path(__file__).parent / "aoc-day7-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

crabs = []

for f in input_array[0].split(","):
    crabs.append(int(f))

crabs.sort()

median_pos = int(len(crabs) / 2)
min_fuel_usage = fuel_usage(crabs, crabs[median_pos])
print ("crabs[" + str(median_pos) + "] (" + str(crabs[median_pos]) + "): " + str(min_fuel_usage))

pos = median_pos - 1
t = fuel_usage(crabs, crabs[pos])
while (t < min_fuel_usage):
    pos -= 1
    min_fuel_usage = t
    t = fuel_usage(crabs, crabs[pos])

print ("crabs[" + str(pos) + "] (" + str(crabs[pos]) + "): " + str(min_fuel_usage))

pos = median_pos + 1
t2 = fuel_usage(crabs, crabs[pos])
print (t2)
while (t2 < min_fuel_usage):
    pos += 1
    min_fuel_usage = t2
    t2 = fuel_usage(crabs, crabs[pos])

print ("crabs[" + str(pos) + "] (" + str(crabs[pos]) + "): " + str(min_fuel_usage))

