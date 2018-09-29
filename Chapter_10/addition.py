#When the user inserts the wrong information you get a TypeError 
#Write a program that prompts for two numbers
#Add them together and print the result
#Catch the type error if either input is not a number


first_number = input("Please enter your first number or 'q' to exit: ")
second_number = input("Please enter your second number or 'q' to exit: ")

try:
    first_number = int(first_number)
    second_number = int(second_number)
except ValueError:
    print("Please enter integer values")
except TypeError:
    print("Please enter integer values")
else:
    addition = first_number + second_number
    print(addition)

