class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine):
        """Initialise name and age attributes."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(self.name.title() + " serves " +
              self.cuisine.title() + " cuisine.")

    def get_customer_numbers(self):
        """Get the number of customers a restaurant has had"""
        print(restaurant.name.title() + " has served " + str(
            restaurant.number_served)
              + " customers today.")

    def open_restaurant(self):
        """Simulate the restaurant opening"""
        print(self.name.title() + " is now open!")

    def set_number_served(self, customers):
        """Set the number of customers a restaurant has served in a night"""
        self.number_served = customers

    def increment_number_served(self, customers):
        """Increment the number of customers a restaurant has served"""
        self.number_served += customers

class IceCreamStand(Restaurant):
    """A simple attempt to model an Ice Cream Stand"""

    def __init__(self, name, cuisine):
        """
        Initialise attributes of the parent class
        Then initialise attributes specific to an Ice Cream stand
        """
        super().__init__(name, cuisine)
        self.flavours = ['vanilla', 'strawberry', 'chocolate', 'pistachio']

    def display_flavours(self):
        print(self.name.title() + " serves the following flavours of ice cream:")
        for flavour in self.flavours:
            print(flavour.title())


restaurant = IceCreamStand('Mister Whippy', 'Gelato')
restaurant.display_flavours()