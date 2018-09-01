#Store a persons name and strip the whitespace from the name

name = "\t\n Hello my name is Ajay \n \n"

name = name.rstrip()
print(name) 

name = name.lstrip()
print(name)

name = "\t \t Hello my name is Ajay \n \n"
name = name.strip()
print(name)
