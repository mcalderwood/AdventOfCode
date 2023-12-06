with open('/Users/matt/Projects/Advent of Code/2020/aoc-day7-input.txt') as my_file:
    bag_rules = my_file.readlines()

contains = {}
bag_counts = {}
all_possible_containers = set()

def count_contained_bags(color):
    if color not in contains:
        bag_counts[color] = 0
        print(color + " bags contain 0 bags")
    else:
        sum = 0
        for container_color in contains[color]:
            if container_color not in bag_counts:
                count_contained_bags(container_color)

            sum += bag_counts[container_color] * contains[color][container_color] + contains[color][container_color]

        print(color + " bags contain " + str(sum) + " bags")
        bag_counts[color] = sum

for rule in bag_rules:
    x = rule.split("bags contain", 1)

    if x[1].strip() == "no other bags.":
        continue

    container_bag_color = x[0].strip()
    contained_bags = x[1].strip().strip(".").split(",")

    if container_bag_color.strip() == "drab green":
        print("drab green")

    for contained_bag in contained_bags:
        y = contained_bag.strip().split(" ", 3)
        quantity = y[0]
        color = y[1] + " " + y[2]

        if container_bag_color not in contains:
            contains[container_bag_color] = {}
        
        contains[container_bag_color][color] = int(quantity)

count_contained_bags("shiny gold")
print(bag_counts["shiny gold"])


    
