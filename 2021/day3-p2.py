import sys
from pathlib import Path

def count_bits(arr, bit):
    count0 = 0
    count1 = 0
    for num in arr:
        if num[bit] == '0':
            count0 += 1
        elif num[bit] == '1':
            count1 += 1
    return (count0, count1)

path = Path(__file__).parent / "aoc-day3-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

oxygen = input_array.copy()
co2 = input_array.copy()

bit = 0
while len(oxygen) > 1:
    (count0, count1) = count_bits(oxygen, bit)

    keep_arr = []
    keep_char = ''
    if count0 > len(oxygen) / 2:
        keep_char = '0'
    else:
        keep_char = '1'

    for num in oxygen:
        if num[bit] == keep_char:
            keep_arr.append(num)
    
    bit += 1
    oxygen = keep_arr

oxygen_rating = int(oxygen[0], 2)

bit = 0
while len(co2) > 1:
    (count0, count1) = count_bits(co2, bit)

    keep_arr = []
    keep_char = ''
    if count1 < len(co2) / 2:
        keep_char = '1'
    else:
        keep_char = '0'

    for num in co2:
        if num[bit] == keep_char:
            keep_arr.append(num)

    bit += 1
    co2 = keep_arr

co2_rating = int(co2[0], 2)
print (oxygen_rating * co2_rating)
