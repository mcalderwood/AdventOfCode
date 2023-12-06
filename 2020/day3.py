with open('/Users/matt/Projects/Advent of Code/2020/aoc-day3-input.txt') as my_file:
    map = my_file.readlines()

map_width = len(map[0]) - 1
#print (map_width)

column = 0
trees_hit = 0
for line in map[2::2]:
    #print (line)
    column += 1
    #print (column)
    if line[column % map_width] == '#':
        trees_hit += 1
     #   print ("Hit")
    
    #if column < 40:
    #    print (column % map_width)
    #else:
    #    break

print (trees_hit)