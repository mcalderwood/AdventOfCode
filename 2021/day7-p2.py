import sys
import re
from pathlib import Path

def fuel_usage(crabs, x):
    sum = 0
    for c in crabs:
        steps = abs(c - x)
        fuel_cost = int((steps + 1) * (steps / 2))
        #print (str(c) + " -> " + str(x) + ": " + str(fuel_cost))
        sum += fuel_cost
    return sum

# 1 1
# 2 3     1 2
# 3 6     1 2 3 
# 4 10    1 2 3 4 
# 5 15    1 2 3 4 5
# 6 21    1 2 3 4 5 6
# 7 28    1 2 3 4 5 6 7
# 8 36    1 2 3 4 5 6 7 8
# 9 45    
# 10 55
# (steps + 1) * (steps / 2)

path = Path(__file__).parent / "aoc-day7-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

crabs = []

for f in input_array[0].split(","):
    crabs.append(int(f))

avg_pos = int(sum(crabs) / len(crabs))
#avg_idx = 0
#for i in range(len(crabs)):
#    avg_idx = i
#    if crabs[i] > avg_pos:
#        break
#print (avg_pos)
#print (len(crabs))
#print (avg_idx)

#for i in range (max(crabs)):
#    fuel = fuel_usage(crabs, )

min_fuel_usage = fuel_usage(crabs, avg_pos)
print ("pos " + str(avg_pos) + ": " + str(min_fuel_usage))
#print ("crabs[" + str(avg_idx) + "] (" + str(crabs[avg_idx]) + "): " + str(min_fuel_usage))
pos = avg_pos - 1
t = fuel_usage(crabs, pos)
print ("pos " + str(pos) + ": " + str(t))
while (t <= min_fuel_usage):
    pos -= 1
    min_fuel_usage = t
    t = fuel_usage(crabs, pos)
    print ("pos " + str(pos) + ": " + str(min_fuel_usage))

# print ("pos " + str(pos+1) + ": " + str(min_fuel_usage))

pos = avg_pos + 1
t2 = fuel_usage(crabs, pos)
print ("pos " + str(pos) + ": " + str(t2))
while (t2 <= min_fuel_usage):
    pos += 1
    min_fuel_usage = t2
    t2 = fuel_usage(crabs, pos)
    print ("pos " + str(pos) + ": " + str(t2))

print ("pos " + str(pos+1) + ": " + str(fuel_usage(crabs, pos+1)))
# print ("pos " + str(pos) + ": " + str(min_fuel_usage))

