import sys
from pathlib import Path

def find_min_distance(dist, sptSet):
    min = sys.maxsize

    for v in range(map_size * map_size):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v
    
    return min_index


path = Path(__file__).parent / "aoc-day15-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

graph = []

input_data_size = len(input_array[0].strip(" \r\n"))
map_size = input_data_size * 5
map = [ [0] * map_size for i in range(map_size)]
sptSet = [False] * (map_size * map_size)
distance_values = [900000] * (map_size*map_size)

d = len(input_array)
for j in range(len(input_array)):
    line_clean = input_array[j].strip(" \r\n")
    #new_line = [0] * (len(line_clean) * 5)
    for i in range(len(line_clean)):
        for n in range(5):
            for m in range(5):
                val = int(line_clean[i]) + m + n
                if val > 9:
                    val -= 9
                #new_line[i + 10 * m] = val
                map[j + input_data_size * n][i + input_data_size * m] = val
    #map.append(new_line)
#map[0][0] = 0
#print (map[499])

for y in range(map_size):
    for x in range(map_size):
        connected_vertices = []
        this_vertex = (y * map_size) + x
        if y < map_size - 1:
            connected_vertices.append((this_vertex + map_size, map[y+1][x]))
        if x < map_size - 1:
            connected_vertices.append((this_vertex + 1, map[y][x+1]))
        if y > 0:
            connected_vertices.append((this_vertex - map_size, map[y-1][x]))
        if x > 0:
            connected_vertices.append((this_vertex - 1, map[y][x-1]))
        graph.append(connected_vertices)


distance_values[0] = 0

for c in range(map_size * map_size):
    if c % 1000 == 0:
        print (c)
    min_dist_vertex = find_min_distance(distance_values, sptSet) 
    sptSet[min_dist_vertex] = True
    for (v, d) in graph[min_dist_vertex]:
        if sptSet[v] == False and distance_values[v] > distance_values[min_dist_vertex] + d:
            distance_values[v] = distance_values[min_dist_vertex] + d

print (distance_values[map_size*map_size-1])
#print (map[0][0])