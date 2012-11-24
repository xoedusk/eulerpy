# test_p14.py
#
# Unit tests for Project Euler problem 14

from p14 import *
import unittest

class CollatzTests(unittest.TestCase):
    def test_known_values(self):
        for method in [1, 2]:
            self.assertEqual(collatz(1, method), [1])
            self.assertEqual(collatz(2, method), [2, 1])
            self.assertEqual(collatz(3, method), [3, 10, 5, 16, 8, 4, 2, 1])
            self.assertEqual(collatz(4, method), [4, 2, 1])
            self.assertEqual(collatz(5, method), [5, 16, 8, 4, 2, 1])
            self.assertEqual(collatz(6, method), [6, 3, 10, 5, 16, 8, 4, 2, 1])
            self.assertEqual(collatz(7, method), [7, 22, 11, 34, 17, 52, 26,
                                                  13, 40, 20, 10, 5, 16, 8, 4,
                                                  2, 1])
            self.assertEqual(collatz(8, method), [8, 4, 2, 1])
            self.assertEqual(collatz(9, method), [9, 28, 14, 7, 22, 11, 34, 17,
                                                  52, 26, 13, 40, 20, 10, 5,
                                                  16, 8, 4, 2, 1])
            self.assertEqual(collatz(10, method), [10, 5, 16, 8, 4, 2, 1])
            self.assertEqual(collatz(13, method), [13, 40, 20, 10, 5, 16, 8, 4,
                                                   2, 1])
    
    def test_method_identical_results(self):
        for n in range(11, 1000):
            self.assertEqual(collatz(n, method=1), collatz(n, method=2))
    
    def test_input_too_low(self):
        for method in [1, 2]:
            self.assertRaises(ValueError, collatz, 0, method)
            self.assertRaises(ValueError, collatz, -1, method)
    
    def test_input_wrong_type(self):
        for method in [1, 2]:
            self.assertRaises(TypeError, collatz, 4.0, method)
            self.assertRaises(TypeError, collatz, '4', method)
    
    def test_bad_method(self):
        for method in [0, 3]:
            self.assertRaises(ValueError, collatz, 4, method)
