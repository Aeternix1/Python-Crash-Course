#IN:

#electric_car.py

from car import Car

class Battery():

class ElectricCar():


#car.py
class Car():

#my_cars.py
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagon', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

#Python offers various ways to complete the same task so you just have to decide
#What works for you

