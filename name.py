name = "ada lovelace"

#You can apply functions to the variables fairly easily
print(name.title())

#Cause you can't trust the Users capitalization input
print(name.upper())
print(name.lower())

#You can add strings together
first_name = "ada"
last_name = "lovelace"
full_name = first_name.title() + ' ' + last_name.title()
print(full_name)

#You can concatenate strings within a function
print("Hello, " + full_name.title() + "!")

#Adding whitespace
print("Python")
print("\tPython\n")
