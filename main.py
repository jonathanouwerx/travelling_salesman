#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 17:00:06 2021

@author: Jonathan
"""
import time

from algorithms import greedy_algorithm, nearest_neighbour_algorithm, brute_force_algorithm
from utils import random_point_generator, create_distance_matrix, draw_circuit
from tsplib_reader import convert_to_lists

######################################################################
# runs a specific algorithm on a specific set of points
def test_algorithm(algorithm, x, y):
    distance_matrix = create_distance_matrix(x,y)
    if algorithm == "Brute Force":
        start = time.time()
        node_order, total = brute_force_algorithm(distance_matrix)
        end = time.time()
        timer = end-start
    elif algorithm == "Nearest Neighbour":
        start = time.time()
        node_order, total = nearest_neighbour_algorithm(distance_matrix)
        end = time.time()
        timer = end-start
    elif algorithm == "Greedy":
        start = time.time()
        node_order, total = greedy_algorithm(distance_matrix)
        end = time.time()
        timer = end-start
    print(algorithm, "Distance:", round(total,3), "Time:", round(timer,6))
    draw_circuit(node_order, total, x, y, algorithm)



######################################################################
# compares the NN and Greedy algorithms to the BF for a specific number of nodes and repeats
def compare_to_bf(num_repeats, num_points):
    distances = []
    bf_timer = 0
    nn_timer = 0
    greedy_timer = 0
    greedy_fail_count = 0
    for _ in range(num_repeats):
        x,y = random_point_generator(num_points)
        distance_matrix = create_distance_matrix(x,y)
        try:
            start = time.time()
            _, greedy_total = greedy_algorithm(create_distance_matrix(x,y))
            end = time.time()
            greedy_timer += end-start
            
            start = time.time()
            _, bf_total = brute_force_algorithm(distance_matrix)
            end = time.time()
            bf_timer += end-start
            
            start = time.time()
            _, nn_total = nearest_neighbour_algorithm(distance_matrix)
            end = time.time()
            nn_timer += end-start
        except:
            greedy_fail_count += 1
        
        # I might need to move the following line into the 'try' section
        distances.append([round(bf_total,3), round(nn_total,3), round(greedy_total,3)])
    
    times = [bf_timer, nn_timer, greedy_timer]
    
    pds = []
    
    for item in distances:
        nn_pd = (item[1]-item[0])/item[0]
        greedy_pd = (item[2]-item[0])/item[0]
        pds.append([nn_pd, greedy_pd])
    
    mean_pd = [0,0]
    for item in pds:
        mean_pd[0] += item[0]
        mean_pd[1] += item[1]
    
    mean_pd[0] = mean_pd[0]/(num_repeats-greedy_fail_count)
    mean_pd[1] = mean_pd[1]/(num_repeats-greedy_fail_count)
        
    print("Total time:", times[0] + times[1] + times[2])
    print("Brute Force Time:", times[0])
    print("Nearest Neigbour Time:", times[1])
    print("Greedy Time:", times[2])
    print("")
    print("Nearest Neighbour percentage difference:", round(100*mean_pd[0],3))
    print("Greedy percentage difference:", round(100*mean_pd[1],3))
    print("")
    print("")

######################################################################
# compares the NN and Greedy algorithms to each other for a specific number of nodes and repeats
def compare_to_each_other(num_repeats, num_points):
    distances = []
    nn_timer = 0
    greedy_timer = 0
    greedy_fail_count = 0
    for _ in range(num_repeats):
        x,y = random_point_generator(num_points)
        distance_matrix = create_distance_matrix(x,y)
        try:
            start = time.time()
            _, greedy_total = greedy_algorithm(create_distance_matrix(x,y))
            end = time.time()
            greedy_timer += end-start

            start = time.time()
            _, nn_total = nearest_neighbour_algorithm(distance_matrix)
            end = time.time()
            nn_timer += end-start
        except:
            greedy_fail_count += 1
        
        # I might need to move the following line into the 'try' section
        distances.append([round(nn_total,3), round(greedy_total,3)])
    
    times = [nn_timer, greedy_timer]
    print(nn_timer, greedy_timer)

    time_ratio = times[1]/times[0]

    distance_pds = []
    distance_mean_pd = 0
    mean_distances = [0,0]
    
    for item in distances:
        distance_pd = (item[0]-item[1])/item[1]
        distance_pds.append(distance_pd)
        distance_mean_pd += distance_pd
        mean_distances[0] += item[0]
        mean_distances[1] += item[1]

    mean_distances[0] = mean_distances[0]/len(distances)
    mean_distances[1] = mean_distances[1]/len(distances)    
    
    distance_multiplier = 1 + (distance_mean_pd/(num_repeats-greedy_fail_count))
    
    #print("Comparison against each other")
    print("Number of nodes:", num_points)    
    #print("Number of repeats:", num_repeats)   
    #print("Total time:", times[0] + times[1])
    print("Nearest Neigbour Time:", times[0])
    print("Greedy Time:", times[1])
    #print("")
    #print("Distance Multiplier:", round(distance_multiplier,3))
    print("Time Ratio:", round(time_ratio,2))

    print("Mean NN distance:", mean_distances[0])
    print("Mean Greedy distance:", mean_distances[1])
    print("")
    
    return mean_distances #[num_points, distance_multiplier, time_ratio]

######################################################################

'''
REDO:

    - 1000 repitions of 10 nodes
    - 200 repitions for nodes 5-100
    - TSPLIB node sets
    - fix comments and results analysis
    

'''


#compare_to_bf(1000, 10)

#data = []
#for i in range(1,6):
    #data.append(compare_to_each_other(100,10*i))
   
#print(data) 
   
#print(compare_to_each_other(100,10))

'''
x,y = [0.174, 0.647, 0.058, 0.533, 0.963, 0.225, 0.308, 0.926, 0.605, 0.481], [0.615, 0.843, 0.178, 0.052, 0.726, 0.225, 0.807, 0.818, 0.083, 0.438]
distance_matrix = [
[0.0, 0.525, 0.452, 0.668, 0.797, 0.393, 0.234, 0.779, 0.685, 0.354],
[0.525, 0.0, 0.888, 0.799, 0.337, 0.748, 0.341, 0.28, 0.761, 0.438],
[0.452, 0.888, 0.0, 0.491, 1.058, 0.173, 0.677, 1.078, 0.555, 0.497],
[0.668, 0.799, 0.491, 0.0, 0.799, 0.353, 0.788, 0.861, 0.078, 0.389],
[0.797, 0.337, 1.058, 0.799, 0.0, 0.892, 0.66, 0.099, 0.736, 0.561],
[0.393, 0.748, 0.173, 0.353, 0.892, 0.0, 0.588, 0.918, 0.406, 0.333],
[0.234, 0.341, 0.677, 0.788, 0.66, 0.588, 0.0, 0.618, 0.783, 0.408],
[0.779, 0.28, 1.078, 0.861, 0.099, 0.918, 0.618, 0.0, 0.802, 0.585],
[0.685, 0.761, 0.555, 0.078, 0.736, 0.406, 0.783, 0.802, 0.0, 0.376],
[0.354, 0.438, 0.497, 0.389, 0.561, 0.333, 0.408, 0.585, 0.376, 0.0]]
'''
#print(x,y)
#for i in distance_matrix:
    #print(i)

'''
num_points = 10

x,y = RPG(num_points)

DC(0, 0, x, y, "Points")
test_algorithm("Brute Force", x, y)
test_algorithm("Nearest Neighbour", x, y)
test_algorithm("Greedy", x, y)
'''
def test_tsplib_sets(filenames):
    for filename in filenames:
        x, y, optimal_node_order, distance = convert_to_lists(filename)
        draw_circuit(0, 0, x, y, filename)
        draw_circuit(optimal_node_order, distance, x, y, 'Optimal')
        print("Optimal Tour", "Distance:", round(distance,3))
        
        test_algorithm("Nearest Neighbour", x, y)
        test_algorithm("Greedy", x, y)

filenames = [
'berlin52',
'att48',
'gr202',
'ch150',
'lin105',
'kroA100',
'rd100',
'bayg29',
'st70',
'ulysses22'
]

test_tsplib_sets(filenames)
