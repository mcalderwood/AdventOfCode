with open('/Users/matt/Projects/Advent of Code/2020/aoc-day6-input.txt') as my_file:
    customs = my_file.readlines()

answers = []
sum = 0
nextlineisfirst = True

for line in customs:
    if line.strip() == "":
        # Process group
        sum += len(answers)
        answers.clear()
        nextlineisfirst = True
    else:
        if nextlineisfirst:
            for c in line.strip():
                answers.append(c)
            nextlineisfirst = False
        else:
            toremove = []
            for c in answers:
                if c not in line.strip():
                    toremove.append(c)
            for c in toremove:
                answers.remove(c)

sum += len(answers)
print (sum)