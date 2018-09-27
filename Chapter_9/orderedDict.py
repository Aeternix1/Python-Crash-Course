#Glossary but without the print statements
from collections import OrderedDict

glossary = OrderedDict()

glossary['loop'] = 'A particular form of boolean'
glossary['if'] = 'Set of values stored sequentially in memory'
glossary['list'] = 'A conditiona statement'
glossary['boolean'] = 'Style is an important part of programming'
glossary['style'] = 'Storing values using a key valye pair'

for key, value in glossary.items():
    print(key + ":" + value + "\n")
