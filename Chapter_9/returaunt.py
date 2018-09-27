#Make a class called restaurant
#Store two attributes a restaurant name and cusine type
#Add an additional attribute called numbers served to the resturant class

class Restaurant():

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.numbers_served = 0

    def describe_restaurant(self):
        print("The restaurant is called " + self.name.title()+ " " + " and serves " + \
self.cuisine)

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, served):
        """Sets the number of people served in the restaurant"""
        if (served >= self.numbers_served):
            self.numbers_served = served
        else:
            print("You're already serving more than that!")

    def increment_number_served(self, served):
        """Increments the number of people served"""
        self.numbers_served += served
    
    def show_number_served(self):
        """Shows the number of people served"""
        print(self.name + " is currently serving " + str(self.numbers_served))

jaggis = Restaurant("jaggis", "indian")

print(jaggis.name.title())
print(jaggis.cuisine.title())

jaggis.describe_restaurant()
jaggis.open_restaurant()

hings = Restaurant("hings", "chinese")
mcdonalds = Restaurant("mcdonalds", "burgers")

mcdonalds.describe_restaurant()
hings.describe_restaurant()

jaggis.set_number_served(10)
jaggis.show_number_served()
jaggis.increment_number_served(25)
jaggis.show_number_served()

