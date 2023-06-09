'''
Random point generator for TSP algorithms
Visualisation tool for hamiltonian circuits
'''

import random
import matplotlib.pyplot as plt

def random_point_generator(point_num):
    random_x = []
    random_y = []

    for i in range(0, point_num):
        random_x.append(round(random.random(),3))
        random_y.append(round(random.random(),3))

    return random_x, random_y

def create_distance_matrix(x,y):
    distance_matrix = []
    for i in range(0,len(x)):
        row = []
        for j in range(0,len(x)):
            distance = ( (x[i]-x[j])**2 + (y[i]-y[j])**2)**(0.5)
            row.append(distance)
            
        distance_matrix.append(row)
    
    return distance_matrix

def draw_circuit(order,x,y):
    plt.scatter(x,y)
    plt.scatter(x[0],y[0], c = 'red', s = 100)
    for i in range(0, len(order)-1):
        plt.plot([x[order[i]], x[order[i+1]]],[y[order[i]], y[order[i+1]]], color = 'blue')


x,y = random_point_generator(10)
plt.scatter(x,y)
plt.scatter(x[0],y[0], c = 'red', s = 100)
plt.show()

matrix = create_distance_matrix(x,y)
print(matrix)

order = [0,4,3,5,2,8,9,7,1,6,0]

draw_circuit(order,x,y)
