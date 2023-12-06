from pathlib import Path
import numpy as np
import re

#a = np.arange(10)
#a.shape = (2,5)
#print(a)
#print(a[0,1])
#exit()

def enhance_image(image):
    global algorithm
    padded_image = np.pad(image, ((2,2),(2,2)), 'constant', constant_values=(image[0,0]))
    new_size = padded_image.shape
    new_image = np.zeros((new_size[0]-2, new_size[1]-2), dtype=int)

    for y in range(1, new_size[0]-1):
        for x in range(1, new_size[1]-1):
            #bit8 = padded_image[x-1,y-1] << 8
            #bit7 = padded_image[x,y-1] << 7
            #bit6 = padded_image[x+1,y-1] << 6
            #bit5 = padded_image[x-1,y] << 5
            #bit4 = padded_image[x,y] << 4
            #bit3 = padded_image[x+1,y] << 3
            #bit2 = padded_image[x-1,y+1] << 2
            #bit1 = padded_image[x,y+1] << 1
            #bit0 = padded_image[x+1,y+1]
            #index = (bit8 << 8) + (bit7 << 7) + bit0
            
            index = (padded_image[y-1,x-1] << 8) + \
                (padded_image[y-1,x] << 7) + \
                (padded_image[y-1,x+1] << 6) + \
                (padded_image[y,x-1] << 5) + \
                (padded_image[y,x] << 4) + \
                (padded_image[y,x+1] << 3) + \
                (padded_image[y+1,x-1] << 2) + \
                (padded_image[y+1,x] << 1) + \
                padded_image[y+1,x+1]
            new_image[y-1,x-1] = 1 if algorithm[index] == '#' else 0
    return new_image

size = 100
#size = 5
path = Path(__file__).parent / "aoc-day20-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

image = np.zeros((size, size), dtype=int)
algorithm = input_array[0].strip(" \r\n")

for line in range(2,size+2):
    for c in range(size):
        image[line-2,c] = 1 if input_array[line][c] == '#' else 0

new_image = enhance_image(image)
new_image2 = enhance_image(new_image)
print(np.sum(new_image2))



