class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine):
        """Initialise name and age attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(self.name.title() + " serves " +
              self.cuisine.title() + " cuisine.")

    def open_restaurant(self):
        """Simulate the restaurant opening"""
        print(self.name.title() + " is now open!")


restaurant = Restaurant('pizza hut', 'italian')
print(restaurant.name.title())
print(restaurant.cuisine.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()