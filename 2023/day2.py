from pathlib import Path

path = Path(__file__).parent / "aoc-day2-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

color_limit = { "red": 12, "green": 13, "blue": 14}

valid_game_id_sum = 0

for line in lines:
#line = lines[1]
    game_id_str, the_sets = line.strip().split(": ")
    game_id = int(game_id_str[5:])

    valid_game = True
    for sets in the_sets.split("; "):
        for color_set in sets.split(", "):
            number, color = color_set.split(' ')

            if int(number) > color_limit[color]:
                valid_game = False
                break

        if not valid_game:
            break

    if valid_game:
        valid_game_id_sum += game_id

print (valid_game_id_sum)
        