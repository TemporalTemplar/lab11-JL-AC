import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertFalse(add(2,3) == 6)
        self.assertEqual(add(-1, 5), 4)
        # self.assertFalse()

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(3523, 2), 3521)

    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(0, 5), 0)
        self.assertEqual(mul(-2, 3), -6)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(9, 3), 3)
        self.assertEqual(div(0, 5), 0)
        self.assertEqual(div(-9, 3), -3)
    # ##########################

    ####### Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(3, 81), 4)
        self.assertAlmostEqual(logarithm(10, 1000), 3)

    def test_log_invalid_base(self):  # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(-1, 2)
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 5), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(-9), "Cannot calculate square root of negative numbers")
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()