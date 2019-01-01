import matplotlib.pyplot as plt

#Produce a scatter square plot for the values 1-1000

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

#Remove outliers with edgecolor command
#Color maps are used to visualise a gradient in the color 
#Pass the list of yvalues through c, cmap=plt.cm.Blues smaller numbers will 
#Have lighter values of blue

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square of Value", fontsize=16)

#Set the range for x and y axis respectively
plt.axis([0, 1100, 0, 1100000])

plt.tick_params(axis="both", which="major", labelsize=14)
plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
