'''
Random point generator for TSP algorithms
Visualisation tool for hamiltonian circuits
'''

import random
import matplotlib.pyplot as plt

def RPG(num_points):
    random_x = []
    random_y = []

    for i in range(0, num_points):
        random_x.append(round(random.random(),3))
        random_y.append(round(random.random(),3))

    return random_x, random_y

def CDM(x,y):
    distance_matrix = []
    for i in range(0,len(x)):
        row = []
        for j in range(0,len(x)):
            distance = ( (x[i]-x[j])**2 + (y[i]-y[j])**2)**(0.5)
            row.append(distance)
            
        distance_matrix.append(row)
    
    return distance_matrix

def DC(order, total, x,y,title):
    plt.figure()
    plt.scatter(x,y)
    plt.scatter(x[0],y[0], c = 'red', s = 100)
    for i in range(0, len(order)-1):
        plt.plot([x[order[i]], x[order[i+1]]],[y[order[i]], y[order[i+1]]], color = 'blue')
    plt.plot([x[order[-1]], x[order[0]]], [y[order[-1]], y[order[0]]])
    plt.title(title)
    plt.annotate('Distance:' + str(round(total, 3)), xy=(0, 1), xytext=(12, -12), va='top',xycoords='axes fraction', textcoords='offset points')