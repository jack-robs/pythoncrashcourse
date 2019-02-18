import unittest
from city_country import city_function

class CitiesTestCase(unittest.TestCase):
    """Test city_function"""
    
    def test_city_country(self):
        """Test input of $city, $country, output 'City, Country"""
        formatted_city_country = city_function('santiago', 'chile', 5)
        self.assertEqual(formatted_city_country, 'Santiago, Chile - population 5')
        
unittest.main()


