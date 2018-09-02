motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#You can easily edit the values in a list
motorcycles[0] = 'ducati'
print(motorcycles)

#If you want to add values use the .append() function 
motorcycles.append("harley")
print(motorcycles)

motorcycles = []
print(motorcycles)

#Use intsert(index, ' ') to insert to a particular index
motorcycles.insert(5, 'ducati')
print(motorcycles)

motorcycles.insert(0, 'Toyota')
print(motorcycles)

#Use del to delete the item from a position on the list 
del motorcycles[1]
print(motorcycles)

#You can also use pop to get rid of the item at the end of the list
#You can use the item after you've popped it
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#The value is that you can now actually make use of the last value in the list
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#The pop value can also be used to specify an index
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print(motorcycles)

#Del is used to completely delete whereas pop allows us to use the variable
#After removing it

#You can actually remove by value instead of index
#Remove doesn't store values like pop
#Remove only removes the first instance of the value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
motorcycles.append('ducati')

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")










