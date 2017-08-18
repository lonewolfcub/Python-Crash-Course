sandwich_orders = ['tuna', 'cheese', 'pastrami', 'spam', 'egg and cress',
                   'spam']

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("Making your " + current_order + " sandwich!")
    finished_sandwiches.append(current_order)

print("\nI've made the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())