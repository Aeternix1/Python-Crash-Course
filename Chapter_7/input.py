#Input stores the value as a variable

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)


# print("\n greeter.py")
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# #making a prompt spread out over a few lings with += on the variable
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print("\n Hello, " + name.title() + "!")

#Use the int function to convert string inputs into numbers
height = input("How tall are you, in inches? ")
height = int(height) 

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


