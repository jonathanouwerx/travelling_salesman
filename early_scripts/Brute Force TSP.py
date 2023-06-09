'''
Exhaustively checks every possible leaf on the state tree

'''


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

node_list = [1,2,3,4,5,6,7]
current_node = 0

def find_shortest_node(current_node, remaining_nodes, distance_matrix):
    previous_node = current_node

    # In the situation where there is only one node left, the program merely adds the cost of going from the
    # current node to that node and then back to node 0
    if len(remaining_nodes) == 1:
        distance = distance_matrix[current_node][remaining_nodes[0]] + distance_matrix[remaining_nodes[0]][0]
        return distance
    # sets some very large arbitary number as the initial 'shortest'
    else:
        current_shortest = 10000000

        # iterates through all the possible next nodes that could be travelled to
        for i in remaining_nodes:
            new_list = remaining_nodes.copy()
            current_node = i
            # removes the selected node from the list of remaining nodes
            new_list.remove(i)
            # recalls the function to find the next shortest node adding the distance from the previous node to this node
            new_shortest = find_shortest_node(current_node, new_list, distance_matrix) + distance_matrix[previous_node][current_node]            
            # if this branch yields a shorter path then it is recorded
            if new_shortest < current_shortest:
                current_shortest = new_shortest

    return current_shortest

shortest = find_shortest_node(current_node, node_list, distance_matrix)
print(shortest)

                
