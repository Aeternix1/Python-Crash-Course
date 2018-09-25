#Movie theatres charge different price depending on a person's age
#<3 free, 3-12 $10, >12 $15

prompt = "What is your age?"
prompt += "Press 'q' to exit: "

age = " "
while (age != 'q'):
    age = input(prompt)
    if (age != 'q'):
        age = int(age)
        if (age < 3):
            ticket = 10
        elif (age <= 12):
            ticket = 10
        elif (age > 12):
            ticket = 15
        print("The ticket is worth $" + str(ticket))


