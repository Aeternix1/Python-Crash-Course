#Writing to an empty file

filename = 'programming.txt'

#Opens the file in write mode which allows us to write to it
#r=read only, w=write, a=append
#write mode will make a new blank file and over writes your previous file
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating games.\n")


#Python can only store strings in a text file, so you need to convert it back
#To a number once you want to use it

