#Lists work well for storing sets of items that change during a program
#Values that cannot change are immutable, an immutable list is called a tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Trying to change a tuple
# dimensions[0] = 250

#You can't change the values in a tuple but you can overwrite them
dimensions = (50, 100)
for dimension in dimensions:
    print(dimension)


