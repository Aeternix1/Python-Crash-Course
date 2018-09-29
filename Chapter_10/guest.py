filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write("List of guests:")
    file_object.write("\n")

guest = ' '
while (guest != 'q'):
    guest = input("Please enter your name (or 'q' to exit the program)")
    if (guest != 'q'):
        with open(filename, 'a') as file_object:
            file_object.write(guest.title())
            file_object.write("\n")
            
    
