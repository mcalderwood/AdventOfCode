with open('/Users/matt/Projects/Advent of Code/2020/aoc-day6-input.txt') as my_file:
    customs = my_file.readlines()

answers = set()
sum = 0
for line in customs:
    if line.strip() == "":
        # Process group
        sum += len(answers)
        answers = set()
    else:
        # Add unique letters
        for c in line.strip():
            answers.add(c)

sum += len(answers)
print (sum)