from pathlib import Path

path = Path(__file__).parent / "aoc-day4-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

point_total = 0
for line in lines:
    card, rest = line.strip().split(':')
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

    points = 0
    for winning_num in winning_numbers:
        for my_num in my_numbers:
            if winning_num == my_num:
                if points == 0:
                    points = 1
                else:
                    points *= 2
    point_total += points


print(point_total)
        