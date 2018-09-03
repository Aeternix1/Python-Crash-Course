rivers=['Tiber', 'Amazon', 'Euphretes', 'Margret']

# value = input("Please enter the name of a river or 'e' to leave the program:\n")
# while (value != 'e'):
    # rivers.append(value.title())
    # value = input("Please enter the name of a river or 'e' to leave the program:\n")
print(rivers)

#Using the reverse function, reverse is just plain reverse
rivers.reverse()
print(rivers)

#Sorted function will sort them a-z
#But won't acutally change the values in the list
print(sorted(rivers))
print(rivers)

#Sort function actually changes the list
rivers.sort()
print(rivers)

#You can actually sort from z-a using reverse
rivers.sort(reverse=True)
print(rivers)


