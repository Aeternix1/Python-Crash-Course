#Write a program that prompts for the user's favourite number
#Use json.dump() to store this number in a file
#Write a separate program that reads in this value and prints the message
#"I know your favourite number! It's ______"

import json

filename = 'favourite_number.json'

try:
    with open(filename) as f_obj:
        numbers = json.load(f_obj)

except FileNotFoundError:
    favourite_number = input("What is your favourite number?")
    with open(filename, 'w') as f_obj:
        json.dump(favourite_number, f_obj)

else: 
    print("Your favourite number is " + numbers)
