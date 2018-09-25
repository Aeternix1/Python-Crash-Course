#Looping through all key value pairs

user_0 = {
    'username': 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

#The selection of the key/value variable is variables
#The method items() returns a list of key-value pairs
#The for loop stores each of these pairs in the two variables provided

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")

#If you want to just have the key
for name in favourite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() + ". I see your favourite language is " + \
                favourite_languages[name].title() +  "!")

#Looping through a dictionaries keys in order
for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#Looping through all of the values in order
print("The following languages have been mentioned:")
for language in sorted(favourite_languages.values()):
    print(language.title())

#Notice how there were many repeats, this is no good
print("The following languages have been mentioned:")
for language in sorted(set(favourite_languages.values())):
    print(language.title())





