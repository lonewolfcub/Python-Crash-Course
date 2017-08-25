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

restaurant = Restaurant('pizza hut', 'italian')
print(restaurant.name.title())
print(restaurant.cuisine.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.get_customer_numbers()

restaurant.number_served = 10
restaurant.get_customer_numbers()

restaurant.set_number_served(20)
restaurant.get_customer_numbers()

restaurant.increment_number_served(10)
restaurant.get_customer_numbers()