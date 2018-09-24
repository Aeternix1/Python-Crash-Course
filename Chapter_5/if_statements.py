#There are various types of if statements

#if conditional test:
#   do something
#Once the condition is passed then the indented line is executed

print("\nvoting.py")

age = 17
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote?")
#if-else statements
else:
    print("Sorry, you are too young to vote")
    print("Please register to vote as soon as you turn 18!")

#if-elif-else chain
print("\namusement_park.py")
if age < 4:
    print("Your admission cost is $0")
elif (age >= 4) and (age <= 18):
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

#Revised version of the code note to self - if things repeat there must be a way
#to condense the information
#You don't need to use else statement if it is just clearer to elif and can
#Prevent issues with malicious data and incorrect input by avoiding the use of
#else

age = 19
print("\namusement_park.py")
if age < 4:
    price = 0
elif (age >= 4) and (age <= 18):
    price = 5
else:
    price = 10
print("Your admission cost is $"+ str(price) + ".")

#Testing multiple conditions
#If you need multiple conditions then use sequential if statements
print("\ntoppings.py")
requeseted_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requeseted_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requeseted_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requeseted_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza")


