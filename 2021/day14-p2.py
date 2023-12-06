from pathlib import Path
from typing import Callable

def get_next_elements(template):
    global rules
    for j in range(2,len(template)):
        if template[0:j] not in rules.keys():
            return template[0:j]
    return template

def expand_elements(elements):
    global rules
    elementPart2 = elements[-2:]
    if len(elements) > 2:
        elementPart1 = elements[:-1]
        new_template = rules[elementPart1] + rules[elementPart2]
        rules[elements] = new_template
        return new_template
    else:
        return rules[elementPart2]

path = Path(__file__).parent / "aoc-day14-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

rules = {}
template = {}
steps = 40
elements = set()

###
# NNCB
#
#NN NC CB
#
#
#
#
#
#NNC -> NCNB
#CB -> CH
#-> B
#
#NCN -> NBCC
#NBC -> NBBB
#CHB -> CBHC
#-> B
#
#NBCC -> NBBB + CN
#CNB -> CCNB
#BBB -> BNBN
#BCB -> BBCH
#BHC -> BHHB
#CB -> CH
# -> B

look_for_rules = False
for line in input_array:
    if line.strip(" \r\n") == "":
        look_for_rules = True
        continue

    if look_for_rules == False:
        template_str = line.strip(" \r\n")
    else:
        (adjacentElements, arrow, newElement) = line.strip(" \r\n").split(' ')
        rules[adjacentElements] = (adjacentElements[0] + newElement, newElement + adjacentElements[1])
        elements.add(newElement)

for i in range(1,len(template_str)):
    pair = template_str[i-1:i+1]
    if pair not in template:
        template[pair] = 0
    template[pair] += 1

for step in range(steps):
    new_template = {}

    for (pair, count) in template.items():
        (newPair1, newPair2) = rules[pair]
        if newPair1 not in new_template:
            new_template[newPair1] = 0
        if newPair2 not in new_template:
            new_template[newPair2] = 0
        new_template[newPair1] += count
        new_template[newPair2] += count

    template = new_template

counts = {}
for (pair, count) in template.items():
    c = pair[0]
    if c not in counts.keys():
        counts[c] = 0
    counts[c] += count
counts[template_str[-1]] += 1
min = -1
max = 0
for count in counts.values():
    if count > max:
        max = count
    if count < min or min == -1:
        min = count

print (min)
print (max)
print (max - min)
exit()