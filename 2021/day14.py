from pathlib import Path

path = Path(__file__).parent / "aoc-day14-input-test.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

rules = {}
template = ""
steps = 10
elements = set()

look_for_rules = False
for line in input_array:
    if line.strip(" \r\n") == "":
        look_for_rules = True
        continue

    if look_for_rules == False:
        template = line.strip(" \r\n")
    else:
        (adjacentElements, arrow, newElement) = line.strip(" \r\n").split(' ')
        rules[adjacentElements] = newElement
        elements.add(newElement)

for step in range(steps):
    new_template = ""
    #i = 0
    #while i < len(template):
    for i in range(1, len(template)):
        elementPair = template[i-1] + template[i]
        new_template += template[i-1] + rules[elementPair]
    new_template += template[-1]
    template = new_template
    
    counts = {}
    for c in template:
        if c not in counts.keys():
            counts[c] = 0
        counts[c] += 1

counts = {}
for c in template:
    if c not in counts.keys():
        counts[c] = 0
    counts[c] += 1
min = len(template)
max = 0
for count in counts.values():
    if count > max:
        max = count
    if count < min:
        min = count

print (max - min)