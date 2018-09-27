#Make a class called restaurant
#Store two attributes a restaurant name and cusine type

class Restaurant():

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print("The restaurant is called " + self.name.title()+ " " + " and serves " + \
self.cuisine)

    def open_restaurant(self):
        print("The restaurant is open")

jaggis = Restaurant("jaggis", "indian")

print(jaggis.name.title())
print(jaggis.cuisine.title())

jaggis.describe_restaurant()
jaggis.open_restaurant()

hings = Restaurant("hings", "chinese")
mcdonalds = Restaurant("mcdonalds", "burgers")

mcdonalds.describe_restaurant()
hings.describe_restaurant()
