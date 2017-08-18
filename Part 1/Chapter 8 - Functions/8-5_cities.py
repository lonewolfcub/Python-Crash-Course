def describe_city(name, country="great britain"):
    """A function to describe the location of cities"""
    print (name.title() + " is in " + country.title())

describe_city(name="london")
describe_city(name='manchester')
describe_city(name='paris', country='france')