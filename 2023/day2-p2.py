from pathlib import Path
from functools import reduce

path = Path(__file__).parent / "aoc-day2-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

color_limit = { "red": 12, "green": 13, "blue": 14}

power_sum = 0

for line in lines:#.split('\n'):
#line = lines[1]
    game_id_str, the_sets = line.strip().split(": ")
    game_id = int(game_id_str[5:])

    min_color_needed = { "red": 0, "green": 0, "blue": 0 }

    for set in the_sets.split("; "):
        for color_set in set.split(", "):
            number, color = color_set.split(' ')

            if int(number) > min_color_needed[color]:
                min_color_needed[color] = int(number)

    power_sum += reduce(lambda x, y: x*y, min_color_needed.values())

print (power_sum)
        