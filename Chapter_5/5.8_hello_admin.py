#Make a list of five or more usernames including the name admin
#Write code that will print a greeting to each user after they
#Login to a website

users = ['John', 'Tina', 'admin', 'Steve', 'Jacob']

for user in users:
    if user == 'admin':
        print("Hello " + user + ",would you like to see a status report?")
    else:
        print("Hello " + user + ",thank you for logging in again")



