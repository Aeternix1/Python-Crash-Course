print("\npizza.py")

def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    for topping in toppings:
        print("-" + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#The *toppings makes an empty tuple called toppings and stores the extent of
#inputs

#Mixing positional and arbitrary arguments



