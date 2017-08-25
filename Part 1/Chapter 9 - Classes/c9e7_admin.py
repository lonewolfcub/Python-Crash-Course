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
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Show privileges for the user"""
        print(self.username + " has the following privileges:")
        for privilege in self.privileges:
            print(privilege.title())


aaskey1 = User('arthur',
               'askey',
               'aaskey1',
               12345,
               'employee',
               'aaskey1@fictiouscompany.com',
               'password123',
               False,
               False)

bbaraca = User('Ba',
               'baracas',
               'bbaraca',
               54321,
               'contractor',
               'pity_the_fool@a_team.com',
               'aintgettingonnodamnplane',
               False,
               True)

cchapli = User('charlie',
               'chaplin',
               'cchapli',
               24582,
               'employee',
               'funny_walk@fictiouscompany.com',
               '12345',
               True,
               False)

ddevito = User('danny',
               'devito',
               'ddevito',
               34798,
               'employee',
               'shortnfunnylooking@fictiouscompany.com',
               'iloveyou',
               False,
               False)

eesteve = User('emilio',
               'estevez',
               'eesteve',
               23524,
               'contractor',
               'weirdlyrelatedtocharliesheen@theeighties.com',
               'dontaskmeaboutmybrother',
               False,
               False)

ffawcet = User('farrah',
               'fawcett',
               'ffawcet',
               43678,
               'employee',
               'worldstopmodel@eightiesvogue.com',
               'password',
               False,
               False)

ggarbo1 = User('greta',
               'garbo',
               'ggarbo1',
               38469,
               'contractor',
               'thegoodolddays@thefourties.com',
               'ishallsaythisonlyonce',
               False,
               False)

admin1 = Admin('Bad',
               'Admin',
               'admin1',
               100001,
               'employee',
               'admin1@fictiouscompany.com',
               'root',
               True,
               False)

admin1.describe_user()
admin1.greet_user()
admin1.show_privileges()