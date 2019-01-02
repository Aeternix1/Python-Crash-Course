import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Generate multiple random walks
while True:
    #Make a random walk and plot the points 
    rw = RandomWalk(5000)
    rw.fill_walk()
   
    #Set the size of the plotting window 
    plt.figure(dpi=128, figsize=(20, 10))

    #Coloring the points
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    
    plt.scatter(rw.x_values[0], rw.y_values[0], color='Red', edgecolor='none',\
            s=5)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], color='Red', edgecolor='none',\
            s=5)

    #Emphasise the first and the last points
    plt.show()


    #Remove the axis === NOT WORKING
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    # plt.axis('off')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

