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


pizza_hut = Restaurant('pizza hut', 'italian')
mcdonalds = Restaurant('mcdonalds', 'american')
las_iguanas = Restaurant('Las Iguanas', 'latin')

pizza_hut.describe_restaurant()
mcdonalds.describe_restaurant()
las_iguanas.describe_restaurant()
