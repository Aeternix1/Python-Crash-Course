#Lists should be plural (add s cunt)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#To access elements in a list you need to select on the index you want to use
print(bicycles[0])

#You can apply any string methods to elements on the list
print(bicycles[0].title())

#Indexes also work backwards so you can use -1 to get to the end of the lis
print(bicycles[-1])
print(bicycles[-2])

#You can use individual values from a list like a variable
message = "My first bicycle was a " + bicycles[-3].title() + "."
print(message)
