from pathlib import Path
from functools import cmp_to_key

class Range:
    def __init__(self, src_start, dest_start, length):
        self.src_start = src_start
        self.dest_start = dest_start
        self.length = length

#def compare(item1, item2):
#    return item1.src_start - item2.src_start

path = Path(__file__).parent / "aoc-day5-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

_, seed_list = lines[0].strip().split(':')
seeds = seed_list.strip().split(' ')

seed_pairs = []
for seed_index in range(0, len(seeds), 2):
    seed_pairs.append(Range(int(seeds[seed_index]), -1, int(seeds[seed_index + 1])))

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

#for map in map_order:
#    maps[map] = sorted(maps[map], key=cmp_to_key(compare))

locations = []

seed_found = False
location = -1
while not seed_found:
    location += 1
    search_number = location
    for map in reversed(map_order):
        for range in maps[map]:
            if search_number >= range.dest_start and search_number < range.dest_start + range.length:
                # number is within range
                search_number = search_number - range.dest_start + range.src_start
                break
    
    for seed_range in seed_pairs:
        if search_number >= seed_range.src_start and search_number < seed_range.src_start + seed_range.length:
            seed_found = True
            break
    if location % 100000 == 0:
        print(location)

print(location)
