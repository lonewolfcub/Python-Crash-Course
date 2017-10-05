prompt = "What toppings would you like you pizza?: "
prompt += "\n "

topping = ""
while topping != "quit":
    topping = input(prompt)

    if topping != "quit":
        print("I'll add " + topping + " to your pizza!")
