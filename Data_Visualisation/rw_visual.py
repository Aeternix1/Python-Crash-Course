import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Generate multiple random walks
while True:
    #Make a random walk and plot the points 
    rw = RandomWalk()
    rw.fill_walk()
   
    #Coloring the points
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,\
            edgecolors='none', s=5)

    #Emphasise the first and the last points
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',\
            s=20)
    plt.scatter(rw.x_values[0], rw.y_values[0], c='red', edgecolors='none',\
            s=20)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

