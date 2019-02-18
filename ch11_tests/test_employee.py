import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee Class"""
    
    def setUp(self):
        """Make an employee to use in tests"""
        self.jack = Employee('jack', 'robertson', 70000)
        
    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.jack.give_raise() #calling function
        self.assertEqual(self.jack.annual_salary, 70101) #asserting the function output is equal to desired output

    def test_custom_raise(self):
        """Test that custom raise of 73 works correctly."""
        self.jack.give_raise(73)
        self.assertEqual(self.jack.annual_salary, 70073)
    
unittest.main()
