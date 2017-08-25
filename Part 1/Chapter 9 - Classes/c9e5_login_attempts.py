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
        print("Name: " + self.first_name.title() + " " + self.last_name.title())
        print("Employee Number: " + str(self.employee_number))
        print("Employee Type: " +self.employee_type.title())
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

aaskey1.describe_user()
aaskey1.greet_user()

bbaraca.describe_user()
bbaraca.greet_user()

cchapli.describe_user()
cchapli.greet_user()

ddevito.describe_user()
ddevito.greet_user()

eesteve.describe_user()
eesteve.greet_user()

ffawcet.describe_user()
ffawcet.greet_user()

ggarbo1.describe_user()
ggarbo1.greet_user()

aaskey1.get_user_login_attempts()
aaskey1.increment_login_attempts()
aaskey1.increment_login_attempts()
aaskey1.increment_login_attempts()
aaskey1.increment_login_attempts()
aaskey1.increment_login_attempts()
aaskey1.increment_login_attempts()
aaskey1.increment_login_attempts()
aaskey1.get_user_login_attempts()
aaskey1.reset_login_attempts()
aaskey1.get_user_login_attempts()