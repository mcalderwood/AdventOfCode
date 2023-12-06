from pathlib import Path

def fold_dots(dots, axis, value):
    new_dots = set()
    for dot in dots:
        (x, y) = dot
        if axis == 'x' and x > value:
            new_dots.add((x - (2 * (x - value)) , y))
        elif axis == 'y' and y > value:
            new_dots.add((x, y - (2 * (y - value))))
        else:
            new_dots.add(dot)
    return new_dots

def print_dots(dots):
    for y in range(6):
        for x in range(41):
            if (x,y) in dots:
                print ('#',end='')
            else:
                print ('.',end='')
        print()

path = Path(__file__).parent / "aoc-day13-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

dots = []

look_for_folds = False
for line in input_array:
    if line.strip(" \r\n") == "":
        look_for_folds = True
        #print_dots(dots)
        continue

    if look_for_folds == False:
        (x, y) = line.strip(" \r\n").split(',')
        dots.append((int(x),int(y)))
    else:
        (foldText, alongText, fold) = line.strip(" \r\n").split(' ')
        (axis, value) = fold.split('=')
        dots = fold_dots(dots, axis, int(value))
        dots_set = set(dots)
        dots = list(dots_set)
        #print()
        #print_dots(dots)

print_dots(dots)
print(len(dots))