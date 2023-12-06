from pathlib import Path
import numpy as np
import re

def roll():
    global die, numRolls
    numRolls += 1
    die += 1
    if die == 101:
        die = 1
    return die

#path = Path(__file__).parent / "aoc-day21-input.txt"
#with open(path) as my_file:
#    input_array = my_file.readlines()

positions = [8, 10]
scores = [0, 0]
die = 0
turn = 0
numRolls = 0

while max(scores) < 1000:
    moves = roll() + roll() + roll()
    positions[turn] += moves
    while positions[turn] >= 11:
        positions[turn] -= 10
    scores[turn] += positions[turn]
    turn += 1
    turn = turn % 2

print (numRolls)
print (min(scores))

print (numRolls * min(scores))