from pathlib import Path
from collections import namedtuple

Race = namedtuple("Race", "time distance")

races = [
    Race(56, 546),
    Race(97, 1927),
    Race(78, 1131),
    Race(75, 1139)
]

#races = [Race(7, 9), Race(15,40), Race(30,200)]

total_ways_to_win = 1

for race in races:
    win_count = 0
    for charge_time in range(race.time):
        if charge_time * (race.time - charge_time) > race.distance:
            win_count += 1
    print(win_count)
    total_ways_to_win *= win_count

print(total_ways_to_win)