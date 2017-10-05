current_users = ['adam', 'bob', 'carol', 'dave', 'eric']
new_users = ['BOB', 'Dave', 'fred', 'george', 'harry']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("I'm sorry, the username " + new_user + " is not available, please enter "
              "another username.")
    else:
        print("The username " + new_user + " is available.")