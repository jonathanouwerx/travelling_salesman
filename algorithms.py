#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def brute_force_algorithm(distance_matrix):
    
    # adds the nodes 1 to (n-1) to a list
    remaining_nodes = []
    for i in range(1,len(distance_matrix)):
        remaining_nodes.append(i)
        
    # initialisation of variables
    current_node = 0
    current_shortest = 1000000
    distance = 0
    current_order = [0]
    best_order = []
    
    # iterative function which iteratively adds and removes nodes
    def find_shortest_node(current_node, remaining_nodes, distance_matrix,
                    current_shortest, distance, current_order, best_order):
        # when we descend to the next tier, the "current" node becomes the previous
        previous_node = current_node
    
        # condition in the function currently has a full tour
        if len(remaining_nodes) == 0:
            # adds the final distance from the end node to the initial node
            distance += distance_matrix[current_node][0]
            current_order.append(0)
            # checks to see if this tour is shortest than all previous tours
            if distance < current_shortest:
                current_shortest = distance
                best_order = current_order.copy()
            # removes the last 0 from the order as the function will now move on
            current_order.pop(-1)
            return current_shortest, current_order, best_order
        
        # calls the function again for every next possible node
        for current_node in remaining_nodes:
            new_list = remaining_nodes.copy()
            current_order.append(current_node)
            distance += distance_matrix[previous_node][current_node]
            # removes the next selected node from list of remaining nodes
            new_list.remove(current_node)
            
            # iterates the function again "descends a tier"
            current_shortest, current_order, best_order = find_shortest_node(current_node,
            new_list, distance_matrix, current_shortest, distance, current_order, best_order)
            
            # removes the last node from the order so the next can be checked instead
            current_order.pop(-1)
            # removes the associated distance
            distance -= distance_matrix[previous_node][current_node]            
    
        return current_shortest, current_order, best_order
    
    # calls the main function
    total, ignore, node_order = find_shortest_node(current_node, remaining_nodes, 
            distance_matrix, current_shortest, distance, current_order, best_order)
    return node_order, total



def greedy_algorithm(distance_matrix):
    # changes the distances from node i to node i to 2 instead of 1
    def remove_zeros(distance_matrix):
        for row in range(0,len(distance_matrix)):
            for item in range(0,len(distance_matrix)):
                if row == item:
                    distance_matrix[row][item] = 2
        return distance_matrix
    
    # lists the edges by size order, shortest first
    def order_distances(matrix):        
        ordered_list = []
        for row in range(len(matrix)):
            for item in range(len(matrix)):
                ordered_list.append([matrix[row][item],row,item])
        ordered_list.sort()
        for i in range(len(ordered_list)):
            ordered_list[i] = [ordered_list[i][1],ordered_list[i][2],
                               ordered_list[i][0]]
        return ordered_list

    distance_matrix = remove_zeros(distance_matrix)
    ordered_list = order_distances(distance_matrix)
    
    total = 0                
    pairs = []
    # appearance count refers to how often each node appears in the current edges
    appearance_count = []
    for i in range(len(distance_matrix)):
        appearance_count.append(0)
    
    # function that adds edges until a full tour is created
    chain_filled = False
    while chain_filled == False:
        # ordered list items are of form [node i, node j, size]
        edge_stats = ordered_list[0]
        appearance_count[edge_stats[0]] += 1
        appearance_count[edge_stats[1]] += 1
        ordered_list.pop(0)
        ordered_list.pop(0)
        dummy_pairs = pairs.copy()
        current_pair = edge_stats[0:2].copy()
        dummy_pairs.append(current_pair) 
        current_node = current_pair[1]
        
        # Start of Constraint Validation Section
            
        # given the current node in the chain, this function finds the next node
        def find_next_pair(dummy_pairs, current_node, current_pair):
            finished = False
            for item in dummy_pairs:
                if finished == False:
                    if current_node == item[0]:
                        current_node = item[1]
                        current_pair = item.copy()
                        finished = True
                    elif current_node == item[1]:
                        current_node = item[0]
                        current_pair = item.copy()
                        finished = True
    
            return current_pair, finished, current_node
        
        chain = [edge_stats[0], edge_stats[1]]
        count = 1
        
        # creates the chain of edges connected to the latest added edge
        while count < len(chain):
            dummy_pairs.remove(current_pair)
            current_pair, finished, current_node = find_next_pair(dummy_pairs, 
                                                    current_node, current_pair)
            if finished == True:
                chain.append(current_node)  
            count += 1
        
        # checks if the chain forms a complete tour and whether it is a full tour
        valid = True
        if chain[-1] == chain[0]:
            if len(chain) < len(distance_matrix)+1:
                valid = False
        
        # checks that every node has more than 2 edges
        chain_filled = True
        for item in appearance_count:
            if item == 3:
                valid = False
            if item != 2:
                chain_filled = False
            
        # End of Constraint Validation Section
        
        # if the new edge was valid, it is implemented
        if valid == True:
            pairs.append(edge_stats[0:2])
            total += edge_stats[2]
            
        # otherwise it undoes the latest addition
        else:
            appearance_count[edge_stats[0]] -= 1
            appearance_count[edge_stats[1]] -= 1

    return chain, total


def nearest_neighbour_algorithm(distance_matrix):

    # adds the numbers 1 to (n-1) to a list
    remaining_nodes = []
    for i in range(1,len(distance_matrix)):
        remaining_nodes.append(i)
        
    # initialisation of variables
    current_node = 0
    total = 0
    node_order = [0]
    
    # finds the next nearest node
    def find_nearest_neighbour(current_node, remaining_nodes, distance_matrix,
                               total, node_order):
        minimum = 2
        # for each node which has not been connected
        for next_node in remaining_nodes:
            # find the distance between this node and that node
            distance = distance_matrix[current_node][next_node]
            # if the distance is the smallest so far, record it as the smallest
            if distance < minimum:
                minimum = distance
                min_node = next_node
        # establushes the next node in the order
        node_order.append(min_node)
        remaining_nodes.remove(min_node)
        current_node = min_node
        total += minimum
        return total, remaining_nodes, node_order, current_node
    
    # finds and adds the next nearest node until there are no nodes remaining
    while len(remaining_nodes) >= 1:
        total, remaining_nodes, node_order, current_node = find_nearest_neighbour(
            current_node, remaining_nodes, distance_matrix, total, node_order)
    
    # adds the final distance back to the starting city
    total += distance_matrix[current_node][0]
    node_order.append(0)

    return node_order, total
