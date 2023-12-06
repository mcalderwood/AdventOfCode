with open('/Users/matt/Projects/Advent of Code/2020/aoc-day5-input.txt') as my_file:
    seatIds = my_file.readlines()

max = 0
for seatId in seatIds:
    seatId = seatId.replace('F','0')
    seatId = seatId.replace('B','1')
    seatId = seatId.replace('L','0')
    seatId = seatId.replace('R','1')

    seatNumber = int(seatId, 2)

    if seatNumber > max:
        max = seatNumber

print (max)
    



