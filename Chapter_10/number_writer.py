import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    #Json dumps data strctures
    json.dump(numbers, f_obj)
