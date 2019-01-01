#A number raised to the third power is a cube
#Plot the first five cubic number, and then plot the first 5000 cubic numbers
import matplotlib.pyplot as plt

x_values=list(range(1,5001))
y_values=[x**3 for x in x_values]

plt.title("Cubed Values", fontsize=14)
plt.xlabel("Values",fontsize=10)
plt.ylabel("Cube of values", fontsize=10)

plt.scatter(x_values, y_values, s=20)
plt.show()
