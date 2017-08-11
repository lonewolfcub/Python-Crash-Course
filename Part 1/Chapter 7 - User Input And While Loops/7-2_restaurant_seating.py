guests = input("How many people are in your dinner party? ")
guests = int(guests)

if guests > 8:
    print("I'm afraid there will be a short wait while we prepare your table.")
else:
    print("Your table is ready, please follow me.")