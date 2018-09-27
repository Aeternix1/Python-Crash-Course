#You want to keep your files as uncluttered as possible
#Python lets you store classes in modules and then import the classes you need
#In the program

from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


