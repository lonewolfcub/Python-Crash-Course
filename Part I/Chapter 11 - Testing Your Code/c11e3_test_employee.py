import unittest
from c11e3_employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """
        Create an employee for use in all tests
        """
        self.first_name = 'Adam'
        self.last_name = 'Min'
        self.annual_salary = 20000

    def test_give_raise(self):
        """Test that the default raise is applied correctly"""
        Employee.give_raise(self)
        self.assertEqual(self.annual_salary, 25000)

    def test_give_custom_raise(self):
        """Test that a custom raise is applied correctly"""
        Employee.give_raise(self, 10000)
        self.assertEqual(self.annual_salary, 30000)


unittest.main()