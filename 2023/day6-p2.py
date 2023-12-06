from pathlib import Path

time = 56977875
distance = 546192711311139

# Test data
#time = 71530
#distance = 940200

total_ways_to_win = 0

start_winning_time = 0
end_winning_time = 0

time_trial = 0
while start_winning_time == 0:
    time_trial += 1
    if time_trial * (time - time_trial) > distance:
        start_winning_time = time_trial

time_trial = time - 1
while end_winning_time == 0:
    time_trial -= 1
    if time_trial * (time - time_trial) > distance:
        end_winning_time = time_trial

print(end_winning_time - start_winning_time + 1)