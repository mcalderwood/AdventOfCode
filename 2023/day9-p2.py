from pathlib import Path
import numpy as np

path = Path(__file__).parent / "aoc-day9-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

def find_prediction(sensor_values):
    if np.all(sensor_values == 0):
        return 0
    else:
        differences = sensor_values[1:] - sensor_values[:-1]
        return sensor_values[0] - find_prediction(differences)

sum = 0
for line in lines:
    sensor_values = np.array([int(i) for i in line.strip().split(" ")])
    #print(sensor_values)
    sum += find_prediction(sensor_values)

print(sum)