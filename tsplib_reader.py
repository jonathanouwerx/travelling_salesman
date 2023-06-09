#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 17:38:23 2021

@author: Jonathan
"""

from utils import draw_circuit, create_distance_matrix

def convert_to_lists(filename):
    x_list = []
    y_list = []
    value_max = 0
    
    tsp_file = open(filename+'.tsp', 'r')
    
    tour_starting = False
    while tour_starting == False:
        line = tsp_file.readline()
        if 'DIMENSION' in line:
            dimension = line.strip().split(':')[1]
        if 'SECTION' in line:
            tour_starting = True
        
    for i in range(0, int(dimension)):
        x,y = tsp_file.readline().strip().split()[1:]
        x_list.append(float(x))
        y_list.append(float(y))
        if float(x) > value_max:
            value_max = float(x)
        if float(y) > value_max:
            value_max = float(y)
    
    tsp_file.close()
    
    limit = value_max *1.0
    
    for i in range(len(x_list)):
        x_list[i] = x_list[i]/limit
        y_list[i] = y_list[i]/limit
    
    # takes the optimal tour from the relevant file
    
    optimal_node_order = []
    
    tsp_file = open(filename+'.opt.tour', 'r')
    
    tour_starting = False
    while tour_starting == False:
        line = tsp_file.readline()
        if 'DIMENSION' in line:
            dimension = line.strip().split(':')[1]
        if 'SECTION' in line:
            tour_starting = True
    
    
    #tsp_file.readline()
    #tsp_file.readline()
    #dimension = tsp_file.readline().strip().split(':')[1] # DIMENSION
    #tsp_file.readline()
    
    
    for i in range(0, int(dimension)):
        point = int(tsp_file.readline())-1
        optimal_node_order.append(int(point))
    
    tsp_file.close()
    
    optimal_node_order.append(0)
    
    distance_matrix = create_distance_matrix(x_list,y_list)
    distance = 0
    for i in range(len(optimal_node_order)-1):
        distance += distance_matrix[optimal_node_order[i]][optimal_node_order[i+1]]
    
    
    return x_list, y_list, optimal_node_order, distance


x,y, optimal_node_order, distance = convert_to_lists('berlin52')

draw_circuit(0, 0, x, y, "Points")
draw_circuit(optimal_node_order, distance, x, y, 'Optimal')

print(optimal_node_order)


