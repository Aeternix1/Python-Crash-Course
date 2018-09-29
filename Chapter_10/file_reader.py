#The open function looks in the directory where the file is stored
#To open the file from another directory you need offer a file path
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#You can store the file path in an absolute file path for more specificity
file_path = '/home/ajay/Documents/Python-Crash-Course/Chapter_10/pi_digits.txt'
with open(file_path) as file_object:
    print(contents.rstrip())

filename = '/home/ajay/Documents/Python-Crash-Course/Chapter_10/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#You can also store a list of lines from a file
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

for line in lines:
    print(line.rstrip())

#You can take the data from the file and you can do things with it
#Python takes all the data as a string, if you want to do something
#With the numbers then you can convert the string using int() or float()
pi_string = ' '
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#Dealing with large files

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    line = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(string))
