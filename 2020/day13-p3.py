with open('/Users/matt/Projects/Advent of Code/2020/aoc-day13-input.txt') as my_file:
    input = my_file.readlines()

# Create array from bus ids.  Index = offset from the mystery timestamp
busIds = []
values = input[1].strip().split(",")
for i in range(len(values)):
    if values[i] != "x":
        busIds.append((int(values[i]),i))

busIds.sort(key=lambda tup: tup[0], reverse=True)
largestBusId, offsetOfLargestBusId = busIds.pop(0)

# Find largest bus id.
#largestBusId = max(busIds)
#indexOfLargestBusId = busIds.index(largestBusId)

print(largestBusId)

#mostBusIds = busIds.copy()
#mostBusIds.remove(largestBusId)
#secondLargest = max(mostBusIds)
#indexOfSecondLargest = busIds.index(secondLargest)
#print(secondLargest)

multiplier = 324
#multiplier = 113000000000
#multiplier = 339750851
answerFound = False
possibleAnswer = 0
threshold = 100000000000
thresholdDelta = 100000000000


# While answer not found :
while not answerFound:
    # Increment multiplier
    multiplier += 797
    answerFound = True

    if possibleAnswer > threshold:
        print(f"{possibleAnswer:,d}", "   m: ", multiplier)
        threshold += thresholdDelta

    # Product = largest bus id * multiplier
    product = largestBusId * multiplier

    # Base possible timestamp = Product - index of largest bus id
    possibleAnswer = product - offsetOfLargestBusId

    # Try next largest
    #if (possibleAnswer + indexOfSecondLargest) % secondLargest != 0:
    #    answerFound = False
    #    continue

    # For each index,busId in bus id array:
    for busId,offset in busIds:

        #if busId == 797 and (possibleAnswer + offset) % busId == 0:
        #    print("first two match!    m: ", multiplier, "  a: ", possibleAnswer)

        # If base possible timestamp + index MOD busId != 0:
        if (possibleAnswer + offset) % busId != 0:
            # Abandon this possible timestamp
            answerFound = False
            break
    
# If this is reached, the timestamp has been found
# Print base timestamp
print(possibleAnswer) 