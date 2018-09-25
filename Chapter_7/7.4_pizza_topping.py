#Loop that prompts the user to enter a series of pizza toppings until they 
#Enter a 'quit' value

prompt = "What is the topping that you want? "
prompt += "\nType 'quit' to end the program "

topping = input(prompt)

while (topping != 'quit'):
    if (topping != 'quit'):
        print("Adding " + topping + " to your pizza!")
        topping = input(prompt)

