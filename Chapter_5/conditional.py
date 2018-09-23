#Conditional statements allow you to check conditions of interest

print("cars.py")

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Conditional test evaluate whether something is true or false
#Distinguish between the two:
car = 'bmw'
if car == 'bmw':
    print("True")
else:
    print("False")
#One sets the variable car to bmw the other checks the equality condition of

car = 'audi'
if car == 'bmw':
    print("True")
else:
    print("False")

#Conditionals are case sensitive if we want to remove this then:
car = 'audi'
if car.lower() == 'audi':
    print("True")
else:
    print("False")

#This sort of check is really valuable when you want to do something like
#Ensure the uniquness of users entered into a website

#The not equal conditional
print("\ntoppings.py")
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")

#Multiple conditions
age_0 = 22
age_1 = 18

if age_0 >= 22 and age_1 >= 21:
    print("True")
else:
    print("False")

