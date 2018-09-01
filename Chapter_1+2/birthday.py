age = 23
#message = "Happy " + age + "rd Birthday!"
#WRONG!

#To ensure that we don't have conflicting types ensure the str() function is
#Used to make the types homogenous  

message = "Happy " + str(age) + "rd Birthday!"
print(message)


