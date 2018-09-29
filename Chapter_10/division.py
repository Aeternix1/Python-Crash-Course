print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: " )
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    #Basically this code will catch the error if it occurs
    #Through try, if it doesn't then it will go to else
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)

    #Current program will crash if you try to divide by zero
     

