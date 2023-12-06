import re

with open('/Users/matt/Projects/Advent of Code/2020/aoc-day14-input.txt') as my_file:
    input = my_file.readlines()

mask_ones = 0
mask_zeroes = 0
mem = {}
current_mask = ''

memInstruction = re.compile(r"mem\[(?P<addr>\d+)\] = (?P<val>\d+)")

#def expand_x

def find_addresses(mask, addr):

    # Apply 1s from mask to addr
    addr_with_ones = addr | int(mask.replace("X","0"),2)
    addr_with_ones_bin_string = f'{addr_with_ones:036b}'
    for pos in range(len(mask)):
        if mask[pos] == 'X':
            addr_with_ones_bin_string = addr_with_ones_bin_string[:pos] + 'X' + addr_with_ones_bin_string[pos+1:]
    new_addr = [addr_with_ones_bin_string]

    # find position of next x in first item in new_addr
    pos = new_addr[0].find('X')
    # while pos is found
    while pos > -1:
        # pop first off new_addr
        a = new_addr.pop(0)

        # push 2 addresses, one with 0 replacing X and one with 1 replacing X
        new_addr.append(a[:pos] + '0' + a[pos+1:])
        new_addr.append(a[:pos] + '1' + a[pos+1:])

        # find position of x in first item in new_addr
        pos = new_addr[0].find('X')

    # Find positions of Xs
    #all_x_pos = [pos for pos, c in mask if c == 'X']
    #for pos, c in mask:
    #    if c == 'X':
    #        for a in new_addr:
    return new_addr


def set_memory(addr, val):
    global current_mask, mem

    addresses = find_addresses(current_mask, addr)
    for a in addresses:
        mem[int(a,2)] = val

    #new_val = (val & mask_zeroes) | mask_ones
    #mem[addr] = new_val

for line in input:
    if line[0:4] == "mask":
        current_mask = line[7:]
    elif line[0:3] == "mem":
        m = memInstruction.match(line)
        set_memory(int(m.group("addr")), int(m.group("val")))
    else:
        print("WTF is ", line)

sum = 0
for val in mem.values():
    sum += val
print(sum)