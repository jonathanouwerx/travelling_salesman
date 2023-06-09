#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 19:23:37 2021

@author: Jonathan
"""

from TSP_Auxilliary import RPG, CDM, DC

def greedy_algorithm_old(distance_matrix):
    for row in range(0,len(distance_matrix)):
            for item in range(0,len(distance_matrix)):
                #distance_matrix[row][item] = round(distance_matrix[row][item], 2)
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
