import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class"""
    
    def setUp(self):
        """Create an instance of employee to run tests on"""
        self.ajay = Employee("Ajay", "Kallukalam", 1000)

    def test_give_default_raise(self):
        self.ajay.give_raise()
        self.assertEqual(6000, self.ajay.salary)

    def test_give_custom_raise(self):
        self.ajay.give_raise(2000)
        self.assertEqual(3000, self.ajay.salary)

unittest.main()
