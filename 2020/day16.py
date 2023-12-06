import re

with open('/Users/matt/Projects/Advent of Code/2020/aoc-day16-input.txt') as my_file:
    input = my_file.readlines()

valid_seats = [False] * 1000

seat_ranges = []
my_ticket = []
nearby_tickets = []
stage = 0
zone_pattern = re.compile(r'(?P<zone_name>[a-z ]+): (?P<seat1_start>\d+)-(?P<seat1_end>\d+) or (?P<seat2_start>\d+)-(?P<seat2_end>\d+)')
#departure location: 25-80 or 90-961

for line in input:
    if line.strip() == "":
        continue
    elif "ticket" in line:
        stage += 1
    elif stage == 0:
        seat_ranges.append(line.strip())
    elif stage == 1:
        my_ticket.append(line.strip())
    elif stage == 2:
        nearby_tickets.append(line.strip())

for zone_entry in seat_ranges:
    m = zone_pattern.search(zone_entry)

    for seat in range(int(m.group('seat1_start')), int(m.group('seat1_end'))):
        valid_seats[seat] = True

    for seat in range(int(m.group('seat2_start')), int(m.group('seat2_end'))):
        valid_seats[seat] = True

sum_bad_seats = 0
for ticket in nearby_tickets:
    for seat in ticket.strip().split(','):
        if not valid_seats[int(seat)]:
            sum_bad_seats += int(seat)

print(sum_bad_seats)
