#Do the following to create a program that simulates how websites ensure that
#Everyone has a unique username

current_users = ['ajay', 'thomas', 'Jayden', 'Marilyn', 'steve', 'matthew']
new_users = ['ajay', 'thomas', 'susan', 'dylan', 'james', 'josh']

#Convert all the current users into lower case 
for x in range(0,len(current_users)):
    current_users[x] = current_users[x].lower()

for new_user in new_users:
    if new_user.lower() in current_users:
        print("That user name is unavailable")
    else:
        print("You can use that username")

