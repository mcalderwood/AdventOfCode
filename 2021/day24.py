from pathlib import Path
import numpy as np
import math
import time

path = Path(__file__).parent / "aoc-day24-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

def get_next_input():
    global input_str
    retvar = input_str[0]
    input_str = input_str[1:]
    return int(retvar)


reg = {
    "w":0,
    "x":0,
    "y":0,
    "z":0
}

input_num = 99999999999961
start_time = time.time()
found_valid_model = False

while not found_valid_model:
    input_str = str(input_num)
    input_num -= 1

    reg["w"] = 0
    reg["x"] = 0
    reg["y"] = 0
    reg["z"] = 0

    if time.time() - start_time > 5:
        print("Model: ", input_num)
        start_time = time.time()

    for line in input_array:
        
        instruction = line[0:3]
        var1 = line[4]

        prev_val = reg.copy()
        #print(line.strip())

        if instruction == "inp":
            reg[var1] = get_next_input()
        
        elif instruction == "add":
            var2 = line[6:].strip()
            if var2 in reg.keys():
                reg[var1] += reg[var2]
            else:
                reg[var1] += int(var2)

        elif instruction == "mul":
            var2 = line[6:].strip()
            if var2 in reg.keys():
                reg[var1] *= reg[var2]
            else:
                reg[var1] *= int(var2)

        elif instruction == "div":
            var2 = line[6:].strip()
            if var2 in reg.keys():
                reg[var1] = math.floor(reg[var1] / reg[var2])
            else:
                reg[var1] = math.floor(reg[var1] / int(var2))

        elif instruction == "mod":
            var2 = line[6:].strip()
            if var2 in reg.keys():
                reg[var1] = reg[var1] % reg[var2]
            else:
                reg[var1] = reg[var1] % int(var2)

        elif instruction == "eql":
            var2 = line[6:].strip()
            if var2 in reg.keys():
                reg[var1] = 1 if reg[var1] == reg[var2] else 0
            else:
                reg[var1] = 1 if reg[var1] == int(var2) else 0

        #print("    w: ", prev_val["w"], "    x: ", prev_val["x"], "    y: ", prev_val["y"], "    z: ", prev_val["z"])
        #print("    w: ", reg["w"], "    x: ", reg["x"], "    y: ", reg["y"], "    z: ", reg["z"])
        #something_changed = False
        #for k in reg.keys():
        #    if reg[k] != prev_val[k]:
        #        print("    ", k, ": ", prev_val[k], " -> ", reg[k])
        #        something_changed = True
        #if not something_changed:
        #    print("    nothing changed")

    if reg["z"] == 0:
        found_valid_model = True
        
 
print(input_num+1)