#List called sandwich_orders and fill it with the names of various sandwiches
#Make empty list called finished_sandwitches
#Loop through the list of sandwich orders and print a message for each order


sandwich_orders = ['tuna', 'pizza', 'beef', 'meatball']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

