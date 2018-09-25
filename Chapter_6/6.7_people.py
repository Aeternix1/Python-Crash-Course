#Make a few people and store all three dictionaries in a list called people
#Print all the information about the people

ajay = {
    'first_name':'ajay',
    'last_name':'kallukalam',
    'age': 22,
    'city':'Sydney',
    }

thomas = {
    'first_name':'thomas',
    'last_name':'kallukalam',
    'age': 51,
    'city':'Sydney',
    }

marilyn = {
    'first_name':'marilyn',
    'last_name':'kallukalam',
    'age': 49,
    'city': 'Sydney',
    }
 
people = [ajay, thomas, marilyn]

for person in people:
    full_name = person['first_name'] + " " +  person['last_name']
    print('Name:' + full_name.title())
    print('Age:'  + str(person['age']))
    print('City:' + person['city'])


