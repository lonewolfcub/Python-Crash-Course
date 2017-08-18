sandwich_orders = ['pastrami', 'tuna', 'cheese', 'pastrami', 'spam', 'egg and cress',
                   'spam', 'pastrami']

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    if current_order == 'pastrami':
        print("I'm afraid we've run out of pastrami!")
        continue
    else:
        print("Making your " + current_order + " sandwich!")
        finished_sandwiches.append(current_order)

print("\nI've made the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())