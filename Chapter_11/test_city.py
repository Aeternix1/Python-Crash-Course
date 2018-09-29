import unittest
from city_function import city_and_country

class NameTestCase(unittest.TestCase):
    """Tests city function"""

    def test_city_and_country(self):
        """Does the city and country"""
        """Santiago Chilie work?"""
        city = city_and_country('santiago', 'chilie')
        self.assertEqual(city, 'Santiago, Chilie')

unittest.main()
