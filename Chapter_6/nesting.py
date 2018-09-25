#Listing allows you to store dictionaries

print("\n aliens.py")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points':10}
alien_2 = {'color': 'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#Randomly generating aliens

print("\n Randomly generating aliens")
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))

#Changing the values of the dictionaries stored in the list
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Use case (d in list) when each dictionary contains lots of information about an
#Object e.g. list of users

print('\n A list inside a dictionary')
#Use case -> When an aspect of an object in the dictionary has multiple
#Information

pizza = { 
    'crust':'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

#Summarise the order
print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the following\
 toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

print('\n Favourite Languages')
favourite_languages = {
        'jen' : ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil' : ['python', 'haskell'],
    }

#Note the use of languages in the key value pair, all values are lists 
for name, languages in favourite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favourite languages is:")
        for language in languages:
            print("\t" + language.title())

    else:
        print("\n" + name.title() + "'s favourite languages are:")
        for language in languages:
            print("\t" + language.title())

#NOTE: Too much nesting is problematic, try to keep it at an understandable
#Level

#Dictionary in a dictionary
print('\n users.py')

users = {
    'aeinstien': {
        'first': 'albert',
        'last': 'einstien',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

#Using the title key will captialise all the values in a sentence
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
   
#Try to ensuer that the structure of nested dictionaries are the same ,
#This makes it much easier to work with


