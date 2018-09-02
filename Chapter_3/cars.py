#We can actually sort a list in a permanent way we use
#.sort() alpha or .sort(reverse=True)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#The sorted list doesn't actually change the order of the list 
#But it does show you a version of the list that A
#Sorted reverse=True can also be used
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

#NOTE: This can become incredibly problematic when you are using UC/LC

print(cars)

cars.reverse()
print(cars)

#The reverse method reverses the order of the list but it doesn not make that
#order alphabetical
cars.reverse()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


