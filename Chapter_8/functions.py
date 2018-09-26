print("\ngreeter.py")
#Define the function called greet_user()
# def greet_user():
    # """Display a simple greeting."""
    # print("Hello!")

# greet_user()

#""" is a docstring which describes what the function does"""

#You can pass variables into a function 
#The variable in the definition is called a parameter
#The variable you use in the function is called an argument

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')

#Positional arguments
# print("\npets.py")
# def describe_pet(animal_type, pet_name):
    # """Display information about a pet"""
    # print("\nI have a " + animal_type + ".")
    # print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#You can call a function as many times as possible
# describe_pet('hamster', 'harry')
# describe_pet("dog", "steve")

#To prevent mistakes with arguments you can use keyword-arugments

# describe_pet(animal_type="hamster", pet_name="harry")

#Just additional syntax, python is looking at the positioning first
# describe_pet(pet_name="hamster", animal_type="harry")

#Default values, mean that the function comes with a strict value in the
#definition

def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('willie')


#The return value returns the function to a variable
print("\nFormatted name")
def get_formatted_name(first_name, last_name):
    """"Return a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#Making an argument optional can also be done in events where you have
#incomplete data 

print("\nfunctions")
def get_formatted_name(first_name, last_name, middle_name = ""):
    if (middle_name):
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " +  last_name
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)
musician = get_formatted_name("john", "hooker", "lee")
print(musician)

#Python interprets non-empty strings as true

#A function can return any kind of value you like including data structures like
#lists and dictionaries

print("\nperson.py")
def build_person(first_name, last_name, age=""):
    """Return a dictionary of information about a person."""
    person = {'first':first_name, 'last': last_name}
    if (age):
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', '22')
print(musician)

#A function can be used with all of the data structures that we have used
print("\n greeter.py")
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if (f_name == 'q'):
        break 

    l_name = input("Last name: ")
    if (l_name == 'q'):
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")



