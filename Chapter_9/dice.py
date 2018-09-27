#Make a class Die with one attribute called sides
#Method roll_die() that prints a random number between  1 and the sides

from random import randint

class Dice():
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        print(str(randint(1,self.sides)))

six = Dice(6)
ten = Dice(10)
twenty = Dice(20) 

for x in range(10):
    six.roll_die()
    ten.roll_die()
    twenty.roll_die()
