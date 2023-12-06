from pathlib import Path

path = Path(__file__).parent / "aoc-day6-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

fish = [0] * 9

for f in input_array[0].split(","):
    fish[int(f)] += 1

for day in range(256):
    fish_birth = fish.pop(0)
    fish[6] += fish_birth
    fish.append(fish_birth)

print (sum(fish))
