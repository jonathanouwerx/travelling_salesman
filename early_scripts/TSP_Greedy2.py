#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 08:41:37 2021

@author: Jonathan
"""


from TSP_Auxilliary import RPG, CDM, DC

#num_points = 10

#x,y = RPG(num_points)
#distance_matrix = CDM(x,y)

def greedy_algorithm2(distance_matrix):
    def remove_zeros(distance_matrix):
        for row in range(0,len(distance_matrix)):
            for item in range(0,len(distance_matrix)):
                #distance_matrix[row][item] = round(distance_matrix[row][item], 3)
                if row == item:
                    distance_matrix[row][item] = 2
        return distance_matrix
    
    def order_distances(matrix):
        ordered_list = []
        while len(ordered_list) < (len(matrix)**2 - len(matrix)):
            minimum = 2
            for row in range(len(matrix)):
                for item in range(len(matrix)):
                    if matrix[row][item] < minimum:
                        minimum = matrix[row][item]
                        min_stats = [row, item, minimum]
            ordered_list.append(min_stats)
            matrix[min_stats[0]][min_stats[1]] = 2
            
        return ordered_list
    
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
    
    for item in distance_matrix:
        print(item)
    
    distance_matrix = remove_zeros(distance_matrix)
    
    for item in distance_matrix:
        print(item)
    
    ordered_list = order_distances(distance_matrix)

    #for item in ordered_list:
        #print(item)
        
    total = 0                
    pairs = []
    appearance_count = []
    for i in range(len(distance_matrix)):
        appearance_count.append(0)
    
    #while len(ordered_list) > 0:
    chain_filled = False
        
    while chain_filled == False:
        edge_stats = ordered_list[0]
        appearance_count[edge_stats[0]] += 1
        appearance_count[edge_stats[1]] += 1
        ordered_list.pop(0)
        ordered_list.pop(0)
        dummy_pairs = pairs.copy()
        current_pair = edge_stats[0:2].copy()
        dummy_pairs.append(current_pair) 
        current_node = current_pair[1]
        
        # checks to make sure a small circuit has not been created
        
        chain = [edge_stats[0], edge_stats[1]]
        count = 1
        while count < len(chain):
            dummy_pairs.remove(current_pair)
            current_pair, finished, current_node = find_next_pair(dummy_pairs, current_node, current_pair)
            if finished == True:
                chain.append(current_node)  
            count += 1
    
        valid = True
        if chain[-1] == chain[0]:
            if len(chain) < len(distance_matrix)+1:
                valid = False
        
        chain_filled = True
        for item in appearance_count:
            if item == 3:
                valid = False
            if item != 2:
                chain_filled = False
            
        
     
        #end of validation section: this needs to be fixed, but also check that the validation is implemented elsewhere
        if valid == True:
            pairs.append(edge_stats[0:2])
            total += edge_stats[2]
        else:
            #print(appearance_count)
            appearance_count[edge_stats[0]] -= 1
            appearance_count[edge_stats[1]] -= 1
            #print(appearance_count)
            #print("")
        
    print(chain)
    print(total)
        #print(valid)
        #for item in ordered_list:
            #print(item)
    return chain, total

#chain, total = greedy_algorithm2(distance_matrix)

#print(chain, total)

#DC(chain, total, x, y, "Greedy2")

'''


from TSP_Auxilliary import RPG, CDM, DC

def greedy_algorithm(distance_matrix):
    for row in range(0,len(distance_matrix)):
            for item in range(0,len(distance_matrix)):
                distance_matrix[row][item] = round(distance_matrix[row][item], 2)
                if row == item:
                    distance_matrix[row][item] = 2
    
    #for row in distance_matrix:
        #print(row)
    #print("")
    total = 0                
    pairs = []
    appearance_count = []
    for i in range(len(distance_matrix)):
        appearance_count.append(0)
    
    def find_smallest_connection(distance_matrix, total):
        minimum = 2
        for row in range(0,len(distance_matrix)-1):
            for item in range(0,len(distance_matrix)):
                if distance_matrix[row][item] < minimum:
                    minimum = distance_matrix[row][item]
                    location = [row, item]
        return minimum, location
    
    while len(pairs) < len(distance_matrix):
        minimum, location = find_smallest_connection(distance_matrix, total)
        appearance_count[location[0]] += 1
        appearance_count[location[1]] += 1
        dummy_pairs = pairs.copy()
        dummy_pairs.append(location) 
        
        # checks to make sure a small circuit has not been created
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
            
        current_pair = location.copy()
        current_node = current_pair[1]
        chain = [location[0], location[1]]
        count = 1
        while count < len(chain):
            dummy_pairs.remove(current_pair)
            current_pair, finished, current_node = find_next_pair(dummy_pairs, current_node, current_pair)
            if finished == True:
                chain.append(current_node)  
            count += 1
    
        valid = True
        if chain[-1] == chain[0]:
            if len(chain) < len(distance_matrix):
                valid = False
            else:
                chain_complete = True
        
     
        #end of validation section: this needs to be fixed, but also check that the validation is implemented elsewhere
        
        if valid == True:
            total += minimum
            distance_matrix[location[0]][location[1]] = 1
            distance_matrix[location[1]][location[0]] = 1
            
            for place in location:
                if appearance_count[place] == 2:
                    for i in range(len(distance_matrix)):
                        distance_matrix[i][place] = 1
                        distance_matrix[place][i] = 1
            pairs.append(location)  
            #print(appearance_count)                     
            #print(location)
            #for row in distance_matrix:
                #print(row)
            #print("")
        else:
            appearance_count[location[0]] -= 1
            appearance_count[location[1]] -= 1
            distance_matrix[location[0]][location[1]] = 1
            distance_matrix[location[1]][location[0]] = 1
    #print(pairs)
    
    return chain, total


num_points = 10

x,y = RPG(num_points)
distance_matrix = CDM(x,y)

chain, total = greedy_algorithm(distance_matrix)
#print(chain, total)

DC(chain, total, x, y, "Greedy")

'''
