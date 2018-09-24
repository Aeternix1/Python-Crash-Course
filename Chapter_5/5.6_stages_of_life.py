#Write an if-elif-else chain that determines a person's stage of life

age = int(input("Please enter an age: "))

if age < 2:
    print("Person is a baby")
elif age < 4:
    print("Person is a toddler")
elif age < 13:
    print("Person is a kid")
elif age < 20:
    print("Person is a teenager")
elif age < 65:
    print("Person is an adult")
else:
    print("Person is an elder")
