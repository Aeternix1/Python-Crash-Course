#Ask a user why they like programming
#Store the reason and the user in a file User :  "     "

filename = 'programming_poll.txt'

with open(filename, 'w') as file_object:
    file_object.write("Users and Reasons")
    file_object.write("\n")

user = ''
while (user != 'q'):
    user = input("Please enter your name: (or 'q' to exit the program)\n")
    if (user != 'q'):
        reason = input("Why did you start programming?: \n")
        with open(filename, 'a') as file_object:
            file_object.write(user.title())
            file_object.write("\n")
            file_object.write(reason.title())
            file_object.write("\n")
    
