import json

favourite_number = input("What is your favourite number? ")

filename = 'favourite_number.json'
with open(filename, 'w') as f_obj:
    json.dump(favourite_number, f_obj)
    print("We'll remember your favorite number when you come back!")