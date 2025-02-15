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
print("\tPython\n\tJava\n\tC\n")

#Stripping Whitespace is really useful to remove whitespace when needed
#The stripping process is used to deal with user input

favourite_language = '\tpython\t'
print(favourite_language)
favourite_language = favourite_language.rstrip() 
print(favourite_language)
favourite_language = favourite_language.lstrip()
print(favourite_language)

favourite_language = '\tpython\t'
favourite_language = favourite_language.strip()
print(favourite_language)


