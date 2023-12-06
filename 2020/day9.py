with open('/Users/matt/Projects/Advent of Code/2020/aoc-day9-input.txt') as my_file:
    strings = my_file.readlines()

numbers = []
for string in strings:
    numbers.append(int(string))

begin = 25
found = True

while found:
    num_to_check = numbers[begin]
    range_to_check = numbers[begin-25:begin]
    found = False

    for i in range(len(range_to_check)-1):
        num1 = range_to_check[i]

        for j in range(i+1,25):
            num2 = range_to_check[j]

            if num1 + num2 == num_to_check:
                found = True

    begin += 1

print(num_to_check)