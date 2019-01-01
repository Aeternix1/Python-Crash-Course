import matplotlib.pyplot as plt 

squares = [1, 4, 9, 16, 25] 

#Set line width, chart title and label axis
plt.plot(squares, linewidth=2)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square of Value", fontsize=16)

#Changes the size of the values on the axis
plt.tick_params(axis="both", labelsize=14)

#plt.show() allows you to view any of the plots that are produced
plt.show()
