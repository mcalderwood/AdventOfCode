from pathlib import Path
import numpy as np
import re

path = Path(__file__).parent / "aoc-day22-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

cube = np.zeros((101, 101, 101), dtype=int)

for line in input_array:
    m = re.match(r"(?P<cmd>on|off)\sx=(?P<xmin>-?\d+)\.\.(?P<xmax>-?\d+),y=(?P<ymin>-?\d+)\.\.(?P<ymax>-?\d+),z=(?P<zmin>-?\d+)\.\.(?P<zmax>-?\d+)\s*", line)

    value = 1 if m.group('cmd') == 'on' else 0

    xmin = int(m.group('xmin')) + 50
    xmax = int(m.group('xmax')) + 50
    ymin = int(m.group('ymin')) + 50
    ymax = int(m.group('ymax')) + 50
    zmin = int(m.group('zmin')) + 50
    zmax = int(m.group('zmax')) + 50

    xmin = max(0, xmin)
    ymin = max(0, ymin)
    zmin = max(0, zmin)
    xmax = min(100, xmax)
    ymax = min(100, ymax)
    zmax = min(100, zmax)

    cube[xmin:xmax+1,ymin:ymax+1,zmin:zmax+1] = value
    #print(cube.sum())

print(cube.sum())