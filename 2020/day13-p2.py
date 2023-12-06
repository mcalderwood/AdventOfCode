with open('/Users/matt/Projects/Advent of Code/2020/aoc-day13-input-tx.txt') as my_file:
    input = my_file.readlines()

# Create array from bus ids.  Index = offset from the mystery timestamp
busIds = []
for busId in input[1].strip().split(","):
    if busId == "x":
        busIds.append(0)
    else:
        busIds.append(int(busId))

# Find largest bus id.
largestBusId = max(busIds)
indexOfLargestBusId = busIds.index(largestBusId)

#multiplier = 113000000000
answerFound = False
possibleAnswer = 0
#threshold = 120000000000
#thresholdDelta = 10000000000
multiplier = 0

# While answer not found :
while not answerFound:
    # Increment multiplier
    multiplier += 1
    answerFound = True

 #   if possibleAnswer > threshold:
  #      print(possibleAnswer)
   #     threshold += thresholdDelta

    # Product = largest bus id * multiplier
    product = largestBusId * multiplier

    # Base possible timestamp = Product - index of largest bus id
    possibleAnswer = product - indexOfLargestBusId

    # For each index,busId in bus id array:
    for i in range(len(busIds)):

        busId = busIds[i]

        # Skip if busId == largestBusId or busId == 'x':
        if busId == largestBusId or busId == 0:
            continue

        # If base possible timestamp + index MOD busId != 0:
        if (possibleAnswer + i) % busId != 0:
            # Abandon this possible timestamp
            answerFound = False
            break
    
# If this is reached, the timestamp has been found
# Print base timestamp
print(possibleAnswer) 