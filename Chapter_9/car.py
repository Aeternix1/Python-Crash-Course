class Car():
    """A simple attempt to represent a Car"""

    def __init__(self, make, model, year):
        """Initialises attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        #A default attribute is one we specify by ourselves 
        #Gets run when you use the init method
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given valye"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def increment_odometer(self, mileage):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += mileage

my_new_car = Car('audi', 'a4' , 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#We can edit an attributes value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#But this is really bad practice, objects should only be edited through a method
my_new_car.update_odometer(7) 
my_new_car.read_odometer()

my_used_car = Car('subaru','outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
