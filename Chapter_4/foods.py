#Copying a list can be completed by slicing
#This is the only way to copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favourte foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friends_foods)

my_foods.append("ice cream")
friends_foods.append("canoli")

print(my_foods)
print(friends_foods)

#Cause setting them as equal actually links them together in the system
my_foods = friends_foods
my_foods.append("chocolate")

print(my_foods)
print(friends_foods)
