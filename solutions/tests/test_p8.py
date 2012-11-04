# test_p8.py
#
# Unit tests for Project Euler problem 8

from p8 import *
import unittest

class LargestProductKnownValues(unittest.TestCase):
    def test_easy_values(self):
        #self.assertEqual(largestProductFromConsecutiveNumbers(0, 1), 0)
        self.assertEqual(largestProductFromConsecutiveNumbers(1234567, 1), 7)
        self.assertEqual(largestProductFromConsecutiveNumbers(1234567, 2), 6*7)
        self.assertEqual(largestProductFromConsecutiveNumbers(1234567, 3), 5*6*7)
        self.assertEqual(largestProductFromConsecutiveNumbers(1234567, 4), 4*5*6*7)
        self.assertEqual(largestProductFromConsecutiveNumbers(12345, 5), 2*3*4*5)
        self.assertEqual(largestProductFromConsecutiveNumbers(123454321, 1), 5)
        self.assertEqual(largestProductFromConsecutiveNumbers(123454321, 2), 4*5)
        self.assertEqual(largestProductFromConsecutiveNumbers(123454321, 3), 4*5*4)
        self.assertEqual(largestProductFromConsecutiveNumbers(123454321, 4),
                    3*4*5*4)
        self.assertEqual(largestProductFromConsecutiveNumbers(6311082, 1), 8)
        self.assertEqual(largestProductFromConsecutiveNumbers(6311082, 2), 6*3)
        self.assertEqual(largestProductFromConsecutiveNumbers(6311083, 3), 6*3)
        self.assertEqual(largestProductFromConsecutiveNumbers(6311083, 4), 6*3)
        self.assertEqual(largestProductFromConsecutiveNumbers(6311083, 5), 0)
        self.assertEqual(largestProductFromConsecutiveNumbers(6311083, 6), 0)
        self.assertEqual(largestProductFromConsecutiveNumbers(65456, 1), 6)
        self.assertEqual(largestProductFromConsecutiveNumbers(65456, 2), 6*5)
        self.assertEqual(largestProductFromConsecutiveNumbers(65456, 3), 6*5*4)
        self.assertEqual(largestProductFromConsecutiveNumbers(65456, 4), 6*5*4*5)
        self.assertEqual(largestProductFromConsecutiveNumbers(65456, 5), 6*5*4*5*6)
        self.assertEqual(largestProductFromConsecutiveNumbers(3830360292, 1), 9)
        self.assertEqual(largestProductFromConsecutiveNumbers(3830360292, 2), 3*8)
        self.assertEqual(largestProductFromConsecutiveNumbers(3830360292, 3), 3*8*3)
        self.assertEqual(largestProductFromConsecutiveNumbers(3830360292, 4), 0)
        self.assertEqual(largestProductFromConsecutiveNumbers(3830360292, 5), 0)
        self.assertEqual(largestProductFromConsecutiveNumbers(3830360292, 10), 0)
        self.assertEqual(largestProductFromConsecutiveNumbers(193703111108, 1), 9)
        self.assertEqual(largestProductFromConsecutiveNumbers(193703111108, 2),
                    9*3)
        self.assertEqual(largestProductFromConsecutiveNumbers(193703111108, 3),
                    9*3*7)
        self.assertEqual(largestProductFromConsecutiveNumbers(193703111108, 4),
                    9*3*7)
        self.assertEqual(largestProductFromConsecutiveNumbers(193703111108, 5),
                    3)
        self.assertEqual(largestProductFromConsecutiveNumbers(193703111108, 6), 0)
        self.assertEqual(largestProductFromConsecutiveNumbers(
            376273647634183738723874830748, 27), 0)
        self.assertEqual(largestProductFromConsecutiveNumbers(
            376273647634183738723874830748, 30), 0)
        
class LargestProductFlexibility(unittest.TestCase):
    def test_little_big_endian_doesnt_matter(self):
        self.assertEqual(largestProductFromConsecutiveNumbers(3873361292, 5),
                    largestProductFromConsecutiveNumbers(2921633783, 5))
        self.assertEqual(largestProductFromConsecutiveNumbers(6947109, 5),
                    largestProductFromConsecutiveNumbers(9017496, 5))
    
    def test_number_strings_are_okay(self):
        self.assertEqual(largestProductFromConsecutiveNumbers("3873361292", 5),
                         largestProductFromConsecutiveNumbers(3873361292, 5),)
        self.assertEqual(largestProductFromConsecutiveNumbers("2921633783", 5),
                         largestProductFromConsecutiveNumbers(3873361292, 5),)
    
    def test_number_as_float_is_okay(self):
        self.assertEqual(largestProductFromConsecutiveNumbers(3873361292.99, 5),
                         largestProductFromConsecutiveNumbers(3873361292, 5),)

class LargestProductBadInput(unittest.TestCase):
    def test_num_factors_too_large(self):
        self.assertRaises(ValueError, largestProductFromConsecutiveNumbers, 123456, 7)
        self.assertRaises(ValueError, largestProductFromConsecutiveNumbers, 5, 2)
        self.assertRaises(ValueError, largestProductFromConsecutiveNumbers, 123, 99)
    
    def test_num_factors_must_be_positive(self):
        self.assertRaises(ValueError, largestProductFromConsecutiveNumbers, 123456, 0)
        self.assertRaises(ValueError, largestProductFromConsecutiveNumbers, 123456, -1)
        self.assertRaises(ValueError, largestProductFromConsecutiveNumbers, 123456, -2)
        self.assertRaises(ValueError, largestProductFromConsecutiveNumbers, 1, 0)
    
    def test_num_negative(self):
        self.assertRaises(ValueError, largestProductFromConsecutiveNumbers, -1256, 3)
        self.assertRaises(ValueError, largestProductFromConsecutiveNumbers, -1256, 3)
        
    def test_float_number(self):
        self.assertRaises(TypeError, largestProductFromConsecutiveNumbers, 1256, 3.0)

