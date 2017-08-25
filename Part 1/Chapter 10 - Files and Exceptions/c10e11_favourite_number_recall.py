import json

# Load username, if it has been stored previously.
# Otherwise, prompt for username and store it.

filename = 'favourite_number.json'

with open(filename) as f_obj:
    favourite_number = json.load(f_obj)
    print("Welcome back, your favourite number is " + favourite_number + "!")