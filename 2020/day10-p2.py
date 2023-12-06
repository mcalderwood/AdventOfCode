with open('/Users/matt/Projects/Advent of Code/2020/aoc-day10-input.txt') as my_file:
    adapter_strings = my_file.readlines()

adapters = [int(i) for i in adapter_strings]

adapters.sort()
lastAdapter = max(adapters)
arrangements = 0

adapterExistance = [False] * (lastAdapter+4)
for i in adapters:
    adapterExistance[i] = True

def FindNextAdapter(jolt):
    global adapters, arrangements

    if jolt == lastAdapter:
        arrangements += 1
        if arrangements % 100000 == 0:
            print(arrangements)
        #print(jolt)
        return

    #print(jolt, ", ", sep='', end='')

    if adapterExistance[jolt + 1]:
        FindNextAdapter(jolt + 1)
    if adapterExistance[jolt + 2]:
        FindNextAdapter(jolt + 2)
    if adapterExistance[jolt + 3]:
        FindNextAdapter(jolt + 3)

if adapterExistance[1]:
    FindNextAdapter(1)
if adapterExistance[2]:
    FindNextAdapter(2)
if adapterExistance[3]:
    FindNextAdapter(3)
print(arrangements)