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
        self.fuel = 0

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

    def add_fuel(self, petrol):
        self.fuel += petrol

#Making an electric car class that does everything a car does AND MORE

#We can use classes(instances) as attributes for complex information
#By placing methods in the appropriate class we tend to section the information
#In a much more understandable way
class Battery():
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=70):
        """Initialise the batteries attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the batteries size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge." 
        print(message)

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        #The super method initialised the electric car class with
        #the child class as a simple cutoff of the car
        #any additional attributes can be defined using methods
        super().__init__(make, model, year)
        self.battery = Battery()

            
   #When modelling the electric car you can be as detailed about
   #Which methods and attributes best define the object
    # def describe_battery(self):
        # """Print a statement describing the battery size"""
        # print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def add_fuel(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")
    
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.add_fuel()
my_tesla.battery.get_range()


