'''
MAIN
Random point generator for TSP algorithms
Visualisation tool for hamiltonian circuits
'''

import random
import matplotlib.pyplot as plt

# Random Point Generator
def random_point_generator(num_points):
    # initializes lists of point coordinates
    random_x = []
    random_y = []

    # adds a random number between 0 and 1 to each list until they are big enough
    for i in range(0, num_points):
        random_x.append(round(random.random(),5))
        random_y.append(round(random.random(),5))

    return random_x, random_y

# Create Distance Matrix
def create_distance_matrix(x,y):
    # initializes distance matrix list
    distance_matrix = []
    
    # finds the distance between every pair of points, adding it to the matrix
    for i in range(0,len(x)):
        row = []
        for j in range(0,len(x)):
            distance = ( (x[i]-x[j])**2 + (y[i]-y[j])**2)**(0.5)
            row.append(round(distance,5)) 
        distance_matrix.append(row)
    
    return distance_matrix

# Draw Circuit
def draw_circuit(order, total, x, y, title):
    # create a figure with just the points
    plt.figure()
    plt.scatter(x,y)
    plt.scatter(x[0],y[0], c = 'red', s = 100)
    plt.title(title)
    
    if (title == 'Greedy') or (title == "Nearest Neighbour") or (title 
                                    == "Brute Force") or (title == "Optimal"):
        # for every point in the order
        for i in range(0, len(order)-1):
            # draw a line between that point and the next one
            plt.plot([x[order[i]], x[order[i+1]]],[y[order[i]], y[order[i+1]]],
                                                                 color = 'blue')
        plt.plot([x[order[-1]], x[order[0]]], [y[order[-1]], y[order[0]]])
        plt.annotate('Distance:' + str(round(total, 3)), xy=(0, 1), xytext=(12, -12),
                     va='top',xycoords='axes fraction', textcoords='offset points')
        