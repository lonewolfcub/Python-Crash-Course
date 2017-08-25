import json

# Load username, if it has been stored previously.
# Otherwise, prompt for username and store it.

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        prompt = "Are you " + username + "?"
        prompt += "\n(Please enter y/n): "
        response = input(prompt)
        if response == 'n':
            get_new_username()
        else:
            print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()