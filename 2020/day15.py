#with open('/Users/matt/Projects/Advent of Code/2020/aoc-day15-input-t1.txt') as my_file:
#    starting_numbers = my_file.readlines()

#puzzle_input = "0,3,6"  # Answer: 436   175594
#puzzle_input = "1,3,2"  # Answer: 1
#puzzle_input = "2,1,3"  # Answer: 10
#puzzle_input = "1,2,3"  # Answer: 27
#puzzle_input = "2,3,1"  # Answer: 78
#puzzle_input = "3,2,1"  # Answer: 438
#puzzle_input = "3,1,2"  # Answer: 1836
puzzle_input = "6,19,0,5,7,13,1"

prev_nums = {}
turn = 0
last_num = -1

starting_numbers = puzzle_input.split(",")

for n in starting_numbers:
    # record prev num
    if last_num >= 0:
        prev_nums[last_num] = turn

    # determine 
    last_num = int(n)
    turn += 1

while turn < 30000000:
    # if last_num has been seen previously, then find difference
    temp = last_num
    if last_num in prev_nums.keys():
        last_num = turn - prev_nums[last_num]
    else:
        last_num = 0
    
    #record prev num
    prev_nums[temp] = turn
    turn += 1

print(last_num)