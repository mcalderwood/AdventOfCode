from pathlib import Path

path = Path(__file__).parent / "aoc-day4-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

matches = [0] * len(lines)

point_total = 0
card = 0
for line in lines:
    card_num, rest = line.strip().split(':')
    winning, mynumbers = rest.strip().split('|')
    winning_numbers = winning.split(' ')
    my_numbers = mynumbers.split(' ')
    try:
        while True:
            winning_numbers.remove('')
    except ValueError:
        pass

    try:
        while True:    
            my_numbers.remove('')
    except ValueError:
        pass

    #matches = 0
    for winning_num in winning_numbers:
        for my_num in my_numbers:
            if winning_num == my_num:
                matches[card] += 1
    card += 1

for card in reversed(range(len(matches))):
    total = 1
    for extra_card in range(matches[card]):
        total += matches[card + extra_card + 1]
    matches[card] = total


print(sum(matches))
        