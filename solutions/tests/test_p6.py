# test_p6.py
#
# Unit tests for Project Euler problem 6

from p6 import *
import unittest

class SumOfSquaresKnownValues(unittest.TestCase):
    def test_easy_values(self):
        self.assertEqual(sumOfSquares([1, 2, 3, 4, 5]),
                         1 + 2**2 + 3**2 + 4**2 + 5**2)
        self.assertEqual(sumOfSquares([5, 6, 7]),
                         5**2 + 6**2 + 7**2)
        self.assertEqual(sumOfSquares([2, 4, 6, 8]),
                         2**2 + 4**2 + 6**2 + 8**2)
        self.assertEqual(sumOfSquares([1]), 1**2)
        self.assertEqual(sumOfSquares([7]), 7**2)
        self.assertEqual(sumOfSquares([]), 0)
        self.assertEqual(sumOfSquares((1, 2, 3, 4)),
                         sumOfSquares([1, 2, 3, 4]))
    
    def test_negative_elements(self):
        self.assertEqual(sumOfSquares([-5, -2, -1]),
                         1**2 + 2**2 + 5**2)
        self.assertEqual(sumOfSquares([-3, 3]),
                         2*3**2)
        self.assertEqual(sumOfSquares([-3, 3, 4]),
                         2*3**2 + 4**2)
    
    def test_zero_element(self):
        self.assertEqual(sumOfSquares([0]), 0)
        self.assertEqual(sumOfSquares([0, 1, 2, 3, 4]),
                         1**2 + 2**2 + 3**2 + 4**2)
        self.assertEqual(sumOfSquares([0, 1, 6, 8, 33]),
                         sumOfSquares([1, 6, 8, 33]))

class SumOfSquaresBadInput(unittest.TestCase):
    def test_bad_input(self):
        self.assertRaises(TypeError, sumOfSquares, ["1"])
        self.assertRaises(TypeError, sumOfSquares, [1, "2"])

class SquareOfSumKnownValues(unittest.TestCase):
    def test_easy_values(self):
        self.assertEqual(squareOfSum([1, 2, 3, 4, 5]),
                         (1 + 2 + 3 + 4 + 5)**2)
        self.assertEqual(squareOfSum([5, 6, 7]),
                         (5 + 6 + 7)**2)
        self.assertEqual(squareOfSum([2, 4, 6, 8]),
                         (2 + 4 + 6 + 8)**2)
        self.assertEqual(squareOfSum([1]), 1**2)
        self.assertEqual(squareOfSum([7]), 7**2)
        self.assertEqual(squareOfSum([]), 0)
        self.assertEqual(squareOfSum((1, 2, 3, 4)),
                         squareOfSum([1, 2, 3, 4]))
    
    def test_negative_elements(self):
        self.assertEqual(squareOfSum([-5, -2, -1]),
                         (-5 + -2 + -1)**2)
        self.assertEqual(squareOfSum([-3, 3]), 0)
        self.assertEqual(squareOfSum([-3, 3, 4]), 4**2)
    
    def test_zero_element(self):
        self.assertEqual(squareOfSum([0]), 0)
        self.assertEqual(squareOfSum([0, 1, 2, 3, 4]),
                         (1 + 2 + 3 + 4)**2)
        self.assertEqual(squareOfSum([0, 1, 6, 8, 33]),
                         squareOfSum([1, 6, 8, 33]))

class SquareOfSumBadInput(unittest.TestCase):
    def test_bad_input(self):
        self.assertRaises(TypeError, squareOfSum, ["1"])
        self.assertRaises(TypeError, squareOfSum, [1, "2"])

class DiffSquareSumSumSquare(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(diffSquareSumSumSquare([1, 2, 3, 4]),
                         (1 + 2 + 3 + 4)**2 - (1**2 + 2**2 + 3**2 + 4**2))
        self.assertEqual(diffSquareSumSumSquare([5, 8, 11]),
                         (5 + 8 + 11)**2 - (5**2 + 8**2 + 11**2))
    
    def test_negative_elements(self):
        self.assertEqual(diffSquareSumSumSquare([-2, -1, 4, 5]),
                         (-2 - 1 + 4 + 5)**2 - (2**2 + 1**1 + 4**2 + 5**2))

class DiffSquareSumSumSquare(unittest.TestCase):
    def test_bad_input(self):
        self.assertRaises(TypeError, squareOfSum, ["1"])
        self.assertRaises(TypeError, squareOfSum, [1, "2"])

