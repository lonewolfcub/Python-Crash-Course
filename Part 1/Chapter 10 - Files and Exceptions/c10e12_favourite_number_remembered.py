import json

# Load favourite number, if it has been stored previously.
# Otherwise, prompt for favourite number and store it.

def get_stored_favourite_number():
    """Get stored favourite_number if available"""
    filename = 'favourite_number.json'
    try:
        with open(filename) as f_obj:
            favourite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favourite_number

def get_new_favourite_number():
    """Prompt for new favourite number"""
    favourite_number = input("What is your favourite number? ")
    filename = 'favourite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(favourite_number, f_obj)
    return favourite_number

def favourite_number():
    """Recall the user's favourite number"""
    favourite_number = get_stored_favourite_number()
    if favourite_number:
        print("Welcome back, your favourite number is "
              + favourite_number + "!")
    else:
        favourite_number = get_new_favourite_number()
        print("We'll remember your favourite number is " + favourite_number +
              " when you come back!")

favourite_number()