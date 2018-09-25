# #The while condition executes code while a certain condition is true

# current_number = 1
# while current_number <= 5:
    # print(current_number)
    # current_number += 1

# #Letting the user choose when to quit

prompt = "\n Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
    # message = input(prompt)
    # print(message)

    # #Ensure that the quit prompt is not printed
    # if message != 'quit':
        # print(message)

#Flags 
#When we have many conditions we want to impose on a while loop
#We can use a flag which alters depending on the conditions it confronts

# active = True
# while active:
    # message = input(prompt)

    # if message == 'quit':
        # active = False
    # else:
        # print(message)

# #The break statement is used to escape any loop
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
    # city = input(prompt)

    # if city == 'quit':
        # break
    # else:
        # print("I'd love to go to " + city.title() + "!")

#Continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#Infinite loops occur when you have a condition that can't be escaped

