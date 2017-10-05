people = {
    'adam': {
        'first_name': 'adam',
        'last_name' : 'appleseed',
        'age': 40,
        'city': 'aldershot',
    },
    'bob': {
        'first_name' : 'bob',
        'last_name' : 'brown',
        'age' : 25,
        'city' : 'birmingham',
    },
    'carol': {
        'first_name' : 'carol',
        'last_name' : 'cook',
        'age': 36,
        'city' : 'cardiff'
    },
}

for person, personal_info in people.items():
    print ("\nPerson: " + person.title())
    full_name = personal_info['first_name'] + " " + personal_info['last_name']
    age = personal_info['age']
    location = personal_info['city']

    print("\tFull Name: " + full_name.title())
    print("\tAge: " + str(age))
    print("\tLocation: " + location.title())