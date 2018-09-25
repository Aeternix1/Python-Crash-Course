#Make a dictionary containing three major rivers and the country each river runs
#through

rivers = {
    'nile':'egypt',
    'amazon':'brazil',
    'niagra':'canada',
    }

for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title())

for key in rivers.keys():
    print(key.title())

for value in rivers.values():
    print(value.title()) 
