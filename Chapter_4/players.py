#Learning how to slice a list 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
#Prints the according to index stopping at n-1
print(players[0:3])
#Prints between index 1-3
print(players[1:4])
#Getting rid of the first slice prints from the start of the index
print(players[:4])
#You can slice from the end of the list, stops at the n-1th index
print(players[2:])
#The negative index can be used, think -nth equal backwards spaces
print(players[-3:])

#Slices allow us to deal with only the subset of the list
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#Exercise 4.10 Slices
print("The first three items in the list are")
print(players[:3])

print("Three items from the middle of the list are")
print(players[1:-1])

print("The last three items in the list are")
print(players[-3:])
