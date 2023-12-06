import sys
import re
import numpy as np
from pathlib import Path
from queue import LifoQueue

path = Path(__file__).parent / "aoc-day10-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

nav = LifoQueue(maxsize=0)

errorValues = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

syntaxErrorScore = 0
for line in input_array:
    for c in line:
        if c == '<' or c == '[' or c == '(' or c == '{':
            nav.put(c)

        elif (c == '>' and nav.queue[-1] == '<') or \
             (c == ']' and nav.queue[-1] == '[') or \
             (c == ')' and nav.queue[-1] == '(') or \
             (c == '}' and nav.queue[-1] == '{'):
            nav.get_nowait()

        elif c == '\r' or c == '\n':
            continue

        else:
            print("Invalid char " + c + " in line! --> ", line)
            syntaxErrorScore += errorValues[c]
            break

print (syntaxErrorScore)