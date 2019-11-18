import unittest

from calculator.polish_calculator import PolishCalculator

class TestPolishCalculator(unittest.TestCase):

    def test_validate_terms(self):

        #Arrange
        calc = PolishCalculator()

        #Act

        #Assert
        self.assertRaises(SyntaxError, calc.validate_terms("())"))
