import sys
import re
#import numpy as np
from pathlib import Path
from queue import LifoQueue

path = Path(__file__).parent / "aoc-day10-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

nav = LifoQueue(maxsize=0)

errorValues = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
closingTags = { '(': ')', '[': ']', '{': '}', '<': '>' }
closingTagScores = { ')': 1, ']': 2, '}': 3, '>': 4 }

#syntaxErrorScore = 0
#incompleteLines = []
scores = []
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
            score = 0
            while not nav.empty():
                closingTag = closingTags[nav.get()]
                score = (5 * score) + closingTagScores[closingTag]
                #print (closingTags[nav.get()], end='')
            #print(score)
            scores.append(score)
            continue

        else:
            while not nav.empty():
                nav.get()
            #print("Invalid char " + c + " in line! --> ", line)
            #syntaxErrorScore += errorValues[c]
            #while nav.empty() == False:
                #print (nav.get(), end='')
            #print()
            break

scores.sort()
print (scores[int(len(scores)/2)])
#print (syntaxErrorScore)
