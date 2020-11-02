import unittest

from Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)