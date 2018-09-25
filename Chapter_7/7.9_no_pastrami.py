#

sandwich_orders = ['tuna', 'pizza', 'beef', 'meatball', 'pastrami', 'pastrami',\
'pastrami']

finished_sandwiches = []

print("Sorry but we have run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)


