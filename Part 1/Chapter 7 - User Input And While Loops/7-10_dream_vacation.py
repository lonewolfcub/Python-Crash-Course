responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?: ")
    response = input("If you could visit one place in the world, where would "
                     "you go?: ")

    responses[name] = response

    repeat = input("Does anyone else want to take the test? (y/n): ")
    if repeat == 'n':
        polling_active = False

print("\n--- Poll results ---")
for name, response in responses.items():
    print(name + " would like to visit " + response + ".")