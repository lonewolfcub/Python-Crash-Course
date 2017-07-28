pizzas = ["Margarita", "Pepperoni", "Hawaiian"]
friend_pizzas=pizzas[:]

pizzas.append("Stromboli")
friend_pizzas.append("Caprese")

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)