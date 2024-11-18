import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        # เพิ่ม
        self.assertEqual(self.calc.add(-2, 1), -1)

    # Add the following test methods to the TestCalculator class:
    def test_substract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(-9, -12), 3)

if __name__ == '__main__':
    unittest.main()