
print("alien.py")

#Dictionary allows us to contain relevant information about an entity
alien_0 = {'color': 'green', 'points': 5}

#We access the values like so
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

#Adding new key value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#To modify values in a dictionary
alien_0['color'] = 'yellow'
print(alien_0)

#Using the dictionary to modify useful values
#depending on the speed of the alien I'm going to move is x units to the right
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'fast':
    x_increment = 3
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'slow':
    x_increment = 1

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0['x_position'])

#Deleting a key value pair
del alien_0['points']

#Dictionaries can also be used to store similar objects
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print(favourite_languages)


