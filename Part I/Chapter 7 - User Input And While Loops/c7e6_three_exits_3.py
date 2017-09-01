prompt = "What toppings would you like you pizza?: "
prompt += "\n "

while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print("I'll add " + topping + " to your pizza!")
