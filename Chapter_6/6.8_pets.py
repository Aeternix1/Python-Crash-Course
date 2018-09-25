#Make dictionary where name of dictionary is the name of a pet

tabby = {
    'name':'tabby',
    'owner_name':'thomas',
    'species':'cat',
    } 

beaky = {
    'name':'beaky',
    'owner_name':'ajay',
    'species':'budgie',
    }

paul = {
    'name':'paul',
    'owner_name':'scientists',
    'species':'octopus',
    }


pets = [tabby, beaky, paul]

for pet in pets:
    print("\n")
    print("Name:" + pet['name'])
    print("Owner:" + pet['owner_name'])
    print("Species:" + pet['species'])




