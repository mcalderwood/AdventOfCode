with open('/Users/matt/Projects/Advent of Code/2020/aoc-day7-input.txt') as my_file:
    bag_rules = my_file.readlines()

contained_by = {}
all_possible_containers = set()

def find_container_bags_for(color):
    if color not in contained_by:
        print("Error: No info about bags containing " + color + " bags")
    else:
        for container_color in contained_by[color]:
            print("Contained by " + container_color)
            all_possible_containers.add(container_color)
            find_container_bags_for(container_color)

for rule in bag_rules:
    x = rule.split("bags contain", 1)
    container_bag_color = x[0].strip()
    contained_bags = x[1].strip().strip(".").split(",")

    for contained_bag in contained_bags:
        y = contained_bag.strip().split(" ", 3)
        quantity = y[0]
        color = y[1] + " " + y[2]
        
        if color not in contained_by:
            contained_by[color] = {}
        
        contained_by[color][container_bag_color] = quantity

find_container_bags_for("shiny gold")
print(len(all_possible_containers))
    
