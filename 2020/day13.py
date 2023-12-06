with open('/Users/matt/Projects/Advent of Code/2020/aoc-day13-input.txt') as my_file:
    input = my_file.readlines()

earliestTime = int(input[0].strip())
allBusIds = input[1].strip()
busIds = []

for busId in allBusIds.split(","):
    if busId == "x":
        continue

    busIds.append(int(busId))

minTime = 9999999
minBusId = 9999

for busId in busIds:
    multiplier = 1
    while busId * multiplier < earliestTime:
        multiplier += 1
    delta = (busId * multiplier) - earliestTime
    if delta < minTime:
        minTime = delta
        minBusId = busId

print(minTime*minBusId) 