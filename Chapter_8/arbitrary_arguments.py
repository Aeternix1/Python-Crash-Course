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
def make_pizza (size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "- inch pizza with the following\
 toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#**variable creates a dictionary instead of a tuple
#Usually with code you want to get the simplest job done then you 
#Don't get scared when you see so many different things going on
#Can make the program more efficient 
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about the user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton',
        field='physics')

print(user_profile)


