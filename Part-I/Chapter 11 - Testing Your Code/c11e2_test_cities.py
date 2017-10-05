import unittest
from c11e2_population import get_formatted_city_country

class NamesTestCase(unittest.TestCase):
    """Tests for c11e2_population"""

    def test_get_formatted_city_country(self):
        """Do values like 'santiago' and 'chile' work?"""
        formatted_city_country = get_formatted_city_country(
            'santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

unittest.main()