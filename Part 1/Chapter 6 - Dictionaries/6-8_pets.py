alex = {
    'name' : 'alex',
    'kind' : 'aardvark',
    'owner' : 'aaron'
    }
brian = {
    'name': 'brian',
    'kind' : 'bat',
    'owner' : 'bethany'
    }
cleo = {
    'name': 'cleo',
    'kind' : 'cat',
    'owner' : 'cletus'
    }
derek = {
    'name': 'derek',
    'kind' : 'dog',
    'owner' : 'deborah'
    }
ellie = {
    'name': 'ellie',
    'kind' : 'eagle',
    'owner' : 'eddie'
    }
frank = {
    'name': 'frank',
    'kind' : 'fish',
    'owner' : 'fred'
    }
greg = {
    'name': 'greg',
    'kind' : 'galah',
    'owner' : 'george'
    }

pets = [alex, brian, cleo, derek, ellie, frank, greg]

for pet in pets:
    name = pet['name']
    kind = pet['kind']
    owner = pet['owner']
    print("Pet Name: " + name.title())
    print("\tType of Pet: " + kind.title())
    print("\tName of owner: " + owner.title() +"\n")
