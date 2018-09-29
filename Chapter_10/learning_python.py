filename = 'learning_python.txt'

#Reading the entire file once
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#Looping over the file object
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#Store in list and looping thorugh
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

