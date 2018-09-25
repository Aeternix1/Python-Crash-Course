pizzas = ['Margherita', 'Pineapple', 'Vegan']

for pizza in pizzas:
    print(pizza.title())
    print("I really like " + pizza + " pizza!")

print("I really like pizza!")

#Exercise 4.11 My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
print(friend_pizzas)
