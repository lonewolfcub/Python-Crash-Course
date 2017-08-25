"""A class to model user attributes"""

class User:
    """A simple attempt to model a user"""

    def __init__(self, first_name, last_name, username, employee_number,
                 employee_type, email, password, admin, banned):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.employee_number = employee_number
        self.employee_type = employee_type
        self.email = email
        self.password = password
        self.admin = admin
        self.banned = banned
        self.login_attempts = 0

    def describe_user(self):
        print("\nUsername: " + self.username)
        print(
            "Name: " + self.first_name.title() + " " + self.last_name.title())
        print("Employee Number: " + str(self.employee_number))
        print("Employee Type: " + self.employee_type.title())
        print("User Email: " + self.email)
        print("Password: " + self.password)
        print("User is Admin: " + str(self.admin))
        print("User is Banned: " + str(self.banned))

    def greet_user(self):
        print("\nHello " + self.first_name.title() + "!")

    def increment_login_attempts(self):
        """Increment a user's login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset a user's login attempts to 0"""
        self.login_attempts = 0

    def get_user_login_attempts(self):
        """Print a user's number of login attempts"""
        print(self.username + " has attempted to log in " +
              str(self.login_attempts) + " times.")