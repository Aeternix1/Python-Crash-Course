#Creating a class called dog
#Dogs have a name and age and sit and roll over(behaviour)

class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")


#The __init__() Method
#A function that's part of a class is called a method
#The __init__ method is a special method that is run whenever you create
#A new instance based on the Dog class.
#Th reason for the underscores is to prevent python from confusing it's own
#Built in methods with the ones that you create


#Every method call passes self which is a reference to the instance itself
#Variables that are accessible through instances like this are called
#attributes

#Our methods need to take in self to access the attributes
#Python will run the init method setting the name to willie and age to 6
my_dog = Dog("willie", 6)

#We can use the dot notation to access the attributes
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog it " + str(my_dog.age) + " years old.")

#We call the methods like so:
my_dog.sit()
my_dog.roll_over()

#you can make as many instances of a class as you like as long as each
#instance has a unique variable name or occupies a single spot in a list


