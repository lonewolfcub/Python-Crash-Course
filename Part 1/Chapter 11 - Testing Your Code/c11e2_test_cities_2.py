import unittest
from c11e2_population_2 import get_formatted_city_country

class NamesTestCase(unittest.TestCase):
    """Tests for c11e2_population_2"""

    def test_get_formatted_city_country(self):
        """Do values like 'santiago' and 'chile' work?"""
        formatted_city_country = get_formatted_city_country(
            'santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do values like 'santiago', 'chile' and '5000000' work?"""
        formatted_city_country = get_formatted_city_country(
            'santiago', 'chile', 5000000)
        self.assertEqual(formatted_city_country,
                         'Santiago, Chile - Population 5000000')

unittest.main()