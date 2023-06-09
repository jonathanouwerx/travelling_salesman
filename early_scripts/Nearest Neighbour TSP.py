'''
Always goes to the nearest neighbour
'''
import random
import matplotlib.plot as plt
from 'TSP RPG.py' import random_point_generator(point_num)

distance_matrix = [
[0,12,3,23,1,5,32,56],
[12,0,9,18,3,41,45,5],
[3,9,0,89,56,21,12,49],
[23,18,89,0,87,46,75,17],
[1,3,56,87,0,55,22,86],
[5,41,21,46,55,0,21,76],
[32,45,12,75,22,21,0,11],
[56,5,49,17,86,76,11,0]
]

remaining_nodes = [1,2,3,4,5,6,7]
current_node = 0
total = 0
node_order = [0]

def find_nearest_neighbour(current_node, remaining_nodes, distance_matrix, total, node_order):
    minimum = 100
    for next_node in remaining_nodes:
        distance = distance_matrix[current_node][next_node]
        if distance < minimum:
            minimum = distance
            min_node = next_node
    node_order.append(min_node)
    remaining_nodes.remove(min_node)
    current_node = min_node
    total += minimum
    return total, remaining_nodes, node_order, current_node

while len(remaining_nodes) >= 1:
    total, remaining_nodes, node_order, current_node = find_nearest_neighbour(current_node, remaining_nodes, distance_matrix, total, node_order)

total += distance_matrix[current_node][0]
print("Distance: ",total)
print(node_order)
