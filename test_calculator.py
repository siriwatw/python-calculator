import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-2, 1), -1)

    def test_substract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
    def test_substravt_negative(self):
        self.assertEqual(self.calc.subtract(-9, -12), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)
    def test_multiply_both_negative(self):
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(9, -3), -3)
    def test_divide_both_negative(self):
        self.assertEqual(self.calc.divide(-12, -3), 4)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)
    def test_modulo_negative(self):
        self.assertEqual(self.calc.modulo(-9, 3), 0)

if __name__ == '__main__':
    unittest.main()