from pathlib import Path

class Range:
    def __init__(self, src_start, dest_start, length):
        self.src_start = src_start
        self.dest_start = dest_start
        self.length = length


path = Path(__file__).parent / "aoc-day5-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

_, seed_list = lines[0].strip().split(':')
seeds = seed_list.strip().split(' ')

maps = {}
currentMap = ""

map_order = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

for line in lines[2:]:
    if line.strip() == "":
        continue

    elif line[0].isalpha():
        currentMap, _ = line.strip().split(' ')
        maps[currentMap] = []
    
    else:
        dest_start, src_start, range_length = line.strip().split(' ')
        maps[currentMap].append(Range(int(src_start), int(dest_start), int(range_length)))

locations = []

for seed in seeds:
    search_number = int(seed)
    for map in map_order:
        for range in maps[map]:
            if search_number >= range.src_start and search_number < range.src_start + range.length:
                # number is within range
                search_number = search_number - range.src_start + range.dest_start
                break
    locations.append(search_number)

print(min(locations))