import unittest
from calculator.operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(2, 3), 5)
        self.assertEqual(subtract(-1, 1), 0)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 5)
        self.assertEqual(multiply(-1, 1), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 3), 5)
        self.assertEqual(divide(-1, 1), 0)
        self.assertEqual(divide(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
