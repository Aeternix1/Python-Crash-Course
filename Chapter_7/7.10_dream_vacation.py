#

print("\n ---- Polling ----")

polling_active = True
vacations = {}

while polling_active:

    name = input("\nWhat is your name? ")
    prompt = "If you could visit one place in the world" 
    prompt += ", where would you go? "
    response = input(prompt)

    vacations[name] = response

    repeat = input("Any other responses? (yes/no) ")
    if (repeat == 'no'):
        polling_active = False

for name, response in vacations.items():
    print(name.title() + " really wants to visit " + response.title())
