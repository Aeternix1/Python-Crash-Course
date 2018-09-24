
alien_color = 'red'

if (alien_color == 'green'):
    points = 5
elif (alien_color == 'yellow'):
    points = 10
elif (alien_color == 'red'):
    points = 15
else:
    print("My program is broken")

print("You have killed the "+ alien_color + " alien you have earned " + str(points) + " points")
