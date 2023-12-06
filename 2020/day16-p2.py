import re
from dataclasses import dataclass

@dataclass
class TicketField:
    name: str
    range1_start: int
    range1_end: int
    range2_start: int
    range2_end: int
    field_num: int = -1

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

fields = []
for zone_entry in seat_ranges:
    m = zone_pattern.search(zone_entry)
    fields.append(TicketField(m.group('zone_name'), int(m.group('seat1_start')), int(m.group('seat1_end')), int(m.group('seat2_start')), int(m.group('seat2_end'))))

    for seat in range(int(m.group('seat1_start')), int(m.group('seat1_end'))):
        valid_seats[seat] = True

    for seat in range(int(m.group('seat2_start')), int(m.group('seat2_end'))):
        valid_seats[seat] = True

sum_bad_seats = 0
good_tickets = []
for ticket in nearby_tickets:
    bad_ticket = False
    for seat in ticket.strip().split(','):
        if not valid_seats[int(seat)]:
            bad_ticket = True
    if not bad_ticket:
        good_tickets.append(ticket)

print(len(good_tickets))
print(len(nearby_tickets))

zones = []
for i in range(20):
    zones.append([])

for ticket in good_tickets:
    s = ticket.strip().split(',')
    for i in range(len(s)):
        zones[i].append(int(s[i]))

matched_zones = []
while len(matched_zones) < 20:
    for field in fields:
        # Figure out what zone this field is
        #print(field.name)
        # Skip if already identified
        if field.field_num > 0:
            continue

        # Loop through zones to find which one fits it
        possible_zones = []
        for i in range(len(zones)):
            if i in matched_zones:
                continue

            zone_is_a_match = True
            for num in zones[i]:
                if num < field.range1_start or (num > field.range1_end and num < field.range2_start) or num > field.range2_end:
                    zone_is_a_match = False
            if zone_is_a_match:
                possible_zones.append(i)
        
        if len(possible_zones) == 1:
            field.field_num = possible_zones[0]
            matched_zones.append(possible_zones[0])

for field in fields:
    print(field.name, "=>", field.field_num)

my_ticket_fields = my_ticket[0].strip().split(',')
answer = int(my_ticket_fields[17]) * int(my_ticket_fields[1]) * int(my_ticket_fields[12]) * int(my_ticket_fields[15]) * int(my_ticket_fields[16]) * int(my_ticket_fields[2])
print(answer)