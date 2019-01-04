from random import randint 

class Die():
    """A Class representing a single die"""

    def __init__(self, num_of_sides=6):
        """Assume 6 sided die"""
        self.num_of_sides=num_of_sides

    def roll(self):
        """Return a random int between 1 and the number of sides"""
        return randint(1, self.num_of_sides)


