with open('/Users/matt/Projects/Advent of Code/2020/aoc-day10-input.txt') as my_file:
    adapter_strings = my_file.readlines()

adapters = [int(i) for i in adapter_strings]

adapters.sort()
lastAdapter = max(adapters)
arrangements = 1

multipliers = [0, 1, 1, 2, 4, 7, 13]

#adapters.insert(0, 0)

prev = 0
diff1 = 0
diff3 = 1
consecutive = 1
for adapter in adapters:
    if adapter - prev == 1:
        consecutive += 1
    elif adapter - prev == 3:
        arrangements *= multipliers[consecutive]
        print(multipliers[consecutive])
        consecutive = 1
    else:
        print("UH OH")
        exit()
    
    prev = adapter
print(multipliers[consecutive])
arrangements *= multipliers[consecutive]

print(arrangements)