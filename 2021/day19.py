from pathlib import Path
import re 
import numpy as np

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

def look_for_overlap(s):
    global scanners, all_beacons_in_s0, orientations

    overlap = {}
    for o in orientations:
        for beacon in scanners[s]:
            if len(overlap.keys()) > 5 and max(overlap.values()) >= 12:
                break

            rotated_beacon = np.matmul(beacon, o)

            for beacon0 in all_beacons_in_s0:                
                diff = beacon0 - rotated_beacon
                if str(diff) not in overlap.keys():
                    overlap[str(diff)] = 0
                overlap[str(diff)] += 1
                if overlap[str(diff)] >= 12:
                    break

        for (k, v) in overlap.items():
            if v >= 12:
                # Insert unique beacons into all_beacons_in_s0
                m = re.match(r"\s*\[\s*(?P<x>-?\d+)\s+(?P<y>-?\d+)\s+(?P<z>-?\d+)\s*\]\s*", k)
                offset = np.array([int(m.group('x')), int(m.group('y')), int(m.group('z'))])
                print(offset, " found in Scanner ", s)
                for beacon in scanners[s]:
                    new_beacon = np.matmul(beacon, o) + offset
                    found = False
                    for b in all_beacons_in_s0:
                        if np.array_equal(b, new_beacon):
                            found = True
                            break
                    if found is False:
                        all_beacons_in_s0.append(new_beacon)
                
                return True
    return False


path = Path(__file__).parent / "aoc-day19-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

scanners = []
beacons = []

for line in input_array:
    if line[0:3] == '---':
        if len(beacons) > 0:
            scanners.append(beacons)
        beacons = []
    
    elif len(line.strip(" \r\n")) > 0:
        (x,y,z) = line.strip(" \r\n").split(",")
        beacons.append(np.array([int(x), int(y), int(z)]))
if len(beacons) > 0:
    scanners.append(beacons)

orientations = [
    # Positive x-axis view
    np.array([[1,0,0],[0,1,0],[0,0,1]]),    #  1, 2, 3
    np.array([[1,0,0],[0,0,1],[0,-1,0]]),   #  1, 3,-2
    np.array([[1,0,0],[0,-1,0],[0,0,-1]]),  #  1,-2,-3
    np.array([[1,0,0],[0,0,-1],[0,1,0]]),   #  1,-3, 2

    # Negative x-axis view
    np.array([[-1,0,0],[0,-1,0],[0,0,1]]),  # -1,-2, 3
    np.array([[-1,0,0],[0,0,1],[0,1,0]]),   # -1, 3, 2
    np.array([[-1,0,0],[0,1,0],[0,0,-1]]),  # -1, 2,-3
    np.array([[-1,0,0],[0,0,-1],[0,-1,0]]), # -1,-3,-2

    # Positive y-axis view
    np.array([[0,1,0],[-1,0,0],[0,0,1]]),   #  2,-1, 3
    np.array([[0,1,0],[0,0,1],[1,0,0]]),    #  2, 3, 1
    np.array([[0,1,0],[1,0,0],[0,0,-1]]),   #  2, 1,-3
    np.array([[0,1,0],[0,0,-1],[-1,0,0]]),  #  2,-3,-1

    # Negative y-axis view
    np.array([[0,-1,0],[1,0,0],[0,0,1]]),   # -2, 1, 3
    np.array([[0,-1,0],[0,0,1],[-1,0,0]]),  # -2, 3,-1
    np.array([[0,-1,0],[-1,0,0],[0,0,-1]]), # -2,-1,-3
    np.array([[0,-1,0],[0,0,-1],[1,0,0]]),  # -2,-3, 1

    # Positive z-axis view
    np.array([[0,0,1],[0,1,0],[-1,0,0]]),   #  3, 2, 1
    np.array([[0,0,1],[-1,0,0],[0,-1,0]]),  #  3,-1,-2
    np.array([[0,0,1],[0,-1,0],[1,0,0]]),   #  3,-2,-1
    np.array([[0,0,1],[1,0,0],[0,1,0]]),    #  3, 1, 2

    # Negative z-axis view
    np.array([[0,0,-1],[0,1,0],[1,0,0]]),   # -3, 2, 1
    np.array([[0,0,-1],[1,0,0],[0,-1,0]]),  # -3, 1,-2
    np.array([[0,0,-1],[0,-1,0],[-1,0,0]]), # -3,-2,-1
    np.array([[0,0,-1],[-1,0,0],[0,1,0]]),  # -3,-1, 2
]

scanners_remaining = [*range(1, len(scanners))]
all_beacons_in_s0 = []

# Add all beacons from Scanner 0
for b in scanners[0]:
    all_beacons_in_s0.append(b)

while len(scanners_remaining) > 0:
    for s in scanners_remaining:
        if look_for_overlap(s):
            scanners_remaining.remove(s)
            break

print(len(all_beacons_in_s0))

