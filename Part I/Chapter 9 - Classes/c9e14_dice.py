from random import randint

class Die:
    """A class modelling a variety of multisided dice"""

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)

d6 = Die(6)

for i in range(0,10):
    d6.roll_die()

d10 = Die(10)

for i in range(0,10):
    d10.roll_die()

d20  = Die(20)

for i in range(0,10):
    d20.roll_die()
