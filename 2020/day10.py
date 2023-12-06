with open('/Users/matt/Projects/Advent of Code/2020/aoc-day10-input.txt') as my_file:
    adapter_strings = my_file.readlines()

adapters = [int(i) for i in adapter_strings]

adapters.sort()

prev = 0
diff1 = 0
diff3 = 1
for adapter in adapters:
    if adapter - prev == 1:
        diff1 += 1
    elif adapter - prev == 3:
        diff3 += 1

    prev = adapter

print("Diffs of 1: ", diff1)
print("Diffs of 3: ", diff3)
print(diff1*diff3)