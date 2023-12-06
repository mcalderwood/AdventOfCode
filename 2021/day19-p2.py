from pathlib import Path
import numpy as np
import re

path = Path(__file__).parent / "day19-scanner-positions.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

scanners = [np.array([0,0,0])] * 36

for line in input_array:
    m = re.match(r"\s*\[\s*(?P<x>-?\d+)\s+(?P<y>-?\d+)\s+(?P<z>-?\d+)\s*\]\s*found in Scanner  (?P<s>\d+)\s*", line)
    scanners[int(m.group('s'))] = np.array([int(m.group('x')), int(m.group('y')), int(m.group('z'))])

max = 0
for s1 in range(len(scanners)):
    for s2 in range(s1+1,len(scanners)):
        if s1 == s2:
            continue
        scanner1 = scanners[s1]
        scanner2 = scanners[s2]
        diff = scanner1 - scanner2
        dist = abs(diff[0]) + abs(diff[1]) + abs(diff[2])
        if dist > max:
            max = dist
print(max)


