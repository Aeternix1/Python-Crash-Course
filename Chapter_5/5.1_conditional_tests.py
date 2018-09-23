#Write a series of conditional tests
#Print a statement describing each test and the preditction of the test

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

#Friends defined as friend1, friend2
friends =["friend" + str(value) for value in range(1,22)]

print("Is 'friend22' in the list? I predict False.")
print('friend22' in friends)

age_00 = 33
age_01 = 45

print("Are the ages between 0 and 100? I predict True")
print((age_00 >= 0 and age_00 <= 100) and (age_01 >= 0 and age_01 <= 100))
        
print("Is 'friend 2' in the list? I predict True.")
print('friend2' in friends)
