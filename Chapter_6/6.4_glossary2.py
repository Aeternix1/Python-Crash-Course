#Glossary but without the print statements

glossary = {
    'loop':'A means to accomplish a process several times',
    'if': 'A particular form of boolean',
    'list': 'set of values stored sequentially in memory',
    'boolean':'a conditional statement',
    'style': 'Style is an important part of programming',
    'dictionary': 'storing values using a key value pair',
    'key' : 'starting term in a glossary',
    'value': 'corresponding value to a key',
    }

for key, value in glossary.items():
    print(key + ":" + value + "\n")
