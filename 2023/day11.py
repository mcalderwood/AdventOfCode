from pathlib import Path
import numpy as np

path = Path(__file__).parent / "aoc-day11-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

galaxies = []

expanded_rows = []
for row in range(len(lines)):
    if (lines[row].find('#') == -1):
        expanded_rows.append(row)
        continue

    for col in range(len(lines[row].strip())):
        if lines[row][col] == '#':
            galaxies.append((row, col))

expanded_cols = []
for col in range(len(lines[0].strip())):
    found_galaxy = False
    for row in range(len(lines)):
        if lines[row][col] == '#':
            found_galaxy = True
            break
    if not found_galaxy:
        expanded_cols.append(col)

sum = 0
for g1 in range(len(galaxies)):
    for g2 in range(g1+1, len(galaxies)):
        path = abs(galaxies[g1][0] - galaxies[g2][0]) + abs(galaxies[g1][1] - galaxies[g2][1])
        for row in expanded_rows:
            if row > min(galaxies[g1][0], galaxies[g2][0]) and row < max(galaxies[g1][0], galaxies[g2][0]):
                path += 1
        for col in expanded_cols:
            ming = min(galaxies[g1][1], galaxies[g2][1])
            maxg = max(galaxies[g1][1], galaxies[g2][1])
            if col > ming and col < maxg:
                path += 1

        #print(g1 + 1, " -> ", g2 + 1, " = ", path)
        sum += path
        #sum += abs(galaxies[g1][0] - galaxies[g2][0]) + abs(galaxies[g1][1] - galaxies[g2][1])

print(sum)