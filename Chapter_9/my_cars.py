# from car import Car
# from electric_car import ElectricCar

# my_beetle = Car('volkswagon', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())

import car
import electric_car
my_beetle = car.Car('volkswagon', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla', 'roadster', '2016')
print(my_tesla.get_descriptive_name())


#Don't use:
#from module_name import *
#FUCKING CONFUSING 
#better use module_name.class_name syntax

#You can spread out your modules by storing classes in several modules
#
