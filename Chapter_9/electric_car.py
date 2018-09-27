#Inheritence takes place when the child class takes all of the methods
#and attributes of the parent class
#The child class can also define new attributes of its own

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

#Making an electric car class that does everything a car does AND MORE

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        #The super method initialised the electric car class with
        #the child class as a simple cutoff of the car
        #any additional attributes can be defined using methods
        super().__init__(make, model, year)
        self.battery_size = 70
   
   #When modelling the electric car you can be as detailed about
   #Which methods and attributes best define the object
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()
