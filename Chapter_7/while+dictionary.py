#To modify values in a list or a dictionary use a while loop not a for loop

print("\n confirmed_users.py")

#Start with users that need to be verified
#and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#Verify each user until there are no more unconfirmed users.
#Move each verified user into the list of confirmed users.

#This list runs as long as the list unconfirmed_users is not empty
while unconfirmed_users:
    current_user = unconfirmed_users.pop() #Pop function removes UC user
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\npets.py")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#Storing user input into a dictionary
print("\nmountain_poll.py")
responses = {} 

#Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #Stores the variables into a dictionary
    responses[name] = response

    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

    #Polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + " would like to climb " + response + ".")

