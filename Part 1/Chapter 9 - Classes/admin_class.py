"""A class to model Adminstrators and their privileges"""

from user_class import User

class Privileges():
    """A simple attempt to model admin privileges"""

    def __init__(self):
        """Initialise admin privileges"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Show privileges for the user"""
        print("This user has the following privileges:")
        for privilege in self.privileges:
            print(privilege.title())

class Admin(User):
    """A simple attempt to model an system administrator"""

    def __init__(self, first_name, last_name, username, employee_number,
                 employee_type, email, password, admin, banned):
        """
        Initialise attributes of parent class.
        Then initialise attributes specific to admin class
        """
        super().__init__(first_name, last_name, username,
                         employee_number, employee_type, email, password,
                         admin, banned)
        self.privileges =  Privileges()