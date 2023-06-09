'''
Exhaustively checks every possible leaf on the state tree

'''

def bf_algorithm(distance_matrix):
    
    remaining_nodes = []
    for i in range(1,len(distance_matrix)):
        remaining_nodes.append(i)
        
    current_node = 0
    current_shortest = 1000000
    distance = 0
    current_order = [0]
    best_order = []
    
    def find_shortest_node(current_node, remaining_nodes, distance_matrix, current_shortest, distance, current_order, best_order):
        previous_node = current_node
    
        if len(remaining_nodes) == 0:
            distance += distance_matrix[current_node][0]
            current_order.append(0)
            if distance < current_shortest:
                current_shortest = distance
                best_order = current_order.copy()
            current_order.pop(-1)
            return current_shortest, current_order, best_order
    
        for current_node in remaining_nodes:
            new_list = remaining_nodes.copy()
            current_order.append(current_node)
            distance += distance_matrix[previous_node][current_node]
            new_list.remove(current_node)
    
            current_shortest, current_order, best_order = find_shortest_node(current_node, new_list, distance_matrix, current_shortest, distance, current_order, best_order)
    
            current_order.pop(-1)
            distance -= distance_matrix[previous_node][current_node]            
    
        return current_shortest, current_order, best_order
    
    total, ignore, node_order = find_shortest_node(current_node, remaining_nodes, distance_matrix, current_shortest, distance, current_order, best_order)
    return node_order, total

'''
from TSP_Auxilliary import RPG, CDM, DC

num_points = 10

x,y = RPG(num_points)
distance_matrix = CDM(x,y)

node_order, total = bf_algorithm(distance_matrix)

DC(node_order, x, y)
print("BF")
print("Distance:", total)
print(node_order)
'''