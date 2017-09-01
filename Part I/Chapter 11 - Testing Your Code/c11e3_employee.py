class Employee():
    """A simple attempt to model the attributes of an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialise attributes to describe an employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, give_raise=5000):
        """Give raise to employee"""
        self.annual_salary += give_raise