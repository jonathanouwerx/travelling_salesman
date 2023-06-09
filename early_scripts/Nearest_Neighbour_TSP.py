'''
Always goes to the nearest neighbour
'''

def nn_algorithm(distance_matrix):
    '''
    Takes in a distance matrix and outputs the node order from the algorithm
    '''     

    remaining_nodes = []
    for i in range(1,len(distance_matrix)):
        remaining_nodes.append(i)
        
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

    return node_order, total
'''
from TSP_Auxilliary import RPG, CDM, DC

num_points = 30

x,y = RPG(num_points)
distance_matrix = CDM(x,y)

node_order, total = nn_algorithm(distance_matrix)

DC(node_order, x, y)
print("NN")
print("Distance:", total)
print(node_order)
'''