with open('/Users/matt/Projects/Advent of Code/2020/aoc-day9-input.txt') as my_file:
    strings = my_file.readlines()

the_sum = 18272118

numbers = []
for string in strings:
    numbers.append(int(string))

range_start = 0
found = False

while not found:
    sum = numbers[range_start]
    i = range_start

    while sum < the_sum:
        i += 1
        sum += numbers[i]

    if sum == the_sum:
        found = True
        min = 9999999999
        max = 0
        for n in numbers[range_start:i+1]:
            if n < min:
                min = n
            if n > max:
                max = n
        print(min + max)
    else:
        range_start += 1

