prompt = "What toppings would you like you pizza?: "
prompt += "\n "

active = True
while active:
    topping = input(prompt)

    if topping == "quit":
        active = False

    else:
        print("I'll add " + topping + " to your pizza!")
