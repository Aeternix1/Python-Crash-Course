# #You can pass complex objects into functions

# print("\ngreet_users.py")
# def greet_users(names):
    # """Print a simple greeting to each user in the list"""
    # for name in names:
        # msg = "Hello, " + name.title() + "!"
        # print(msg)


# usernames = ['margot', 'ty', 'robbie']
# greet_users(usernames)

#Two functions that do a specific job each
#Function 1: move all unprinted designs to completed designs
def print_models(unprinted_designs, completed_designs):
    """
    Simulate printing
    Move completed designs to the completed designs list
    """
    while (unprinted_designs):
        design = unprinted_designs.pop()
        completed_designs.append(design)

#Function 2: show completed designs in order
def show_completed_models(completed_designs):
    """Show all the models that were completed"""
    print("\nThe following models have been completed")
    for completed_model in completed_designs:
        print(completed_model)

unprinted_designs = ['iphone_case', 'dodecahedron', 'robot pendent']
completed_model = []

print_models(unprinted_designs, completed_model)
show_completed_models(completed_model)


#The rule of functions is that every function should have one specific job
#Ensuring that over time the pieces of the function are more reusable
#Sometimes you need to ensure that you keep the original list, so
#You should pass through a copy 

#function_name(list_name[:])

#Don't use copies unless you have to, uses up lots of time and memory
print_models(unprinted_designs[:], completed)



