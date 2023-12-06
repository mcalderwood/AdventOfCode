import re

with open('/Users/matt/Projects/Advent of Code/2020/aoc-day14-input.txt') as my_file:
    input = my_file.readlines()

mask_ones = 0
mask_zeroes = 0
mem = {}

memInstruction = re.compile(r"mem\[(?P<addr>\d+)\] = (?P<val>\d+)")

def parse_mask(mask):
    global mask_ones, mask_zeroes
    mask_ones = int(mask.replace("X","0"),2)
    mask_zeroes = int(mask.replace("X","1"),2)

def set_memory(addr, val):
    global mask_ones, mask_zeroes, mem
    new_val = (val & mask_zeroes) | mask_ones
    mem[addr] = new_val

for line in input:
    if line[0:4] == "mask":
        parse_mask(line[7:])
    elif line[0:3] == "mem":
        m = memInstruction.match(line)
        set_memory(int(m.group("addr")), int(m.group("val")))
    else:
        print("WTF is ", line)

sum = 0
for val in mem.values():
    sum += val
print(sum)