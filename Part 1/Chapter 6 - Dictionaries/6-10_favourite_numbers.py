favourite_numbers = {
    'adam': [5 , 10],
    'bob': [7, 15, 72],
    'carol': [3, 23, 54],
    'dave': [9, 35, 88],
    'eric': [4],
}

for name, numbers in favourite_numbers.items():
    if len(numbers) == 1:
        print("\n" + name.title() + "'s favourite number is:")
    else:
        print("\n" + name.title() + "'s favourite numbers are:")
    for number in numbers:
        print(number)