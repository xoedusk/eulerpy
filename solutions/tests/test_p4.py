# test_p4.py
#
# Unit tests for Project Euler, problem 4

from p4 import *
import unittest

class IsPalindromeKnownValues(unittest.TestCase):
    def test_known_values(self):
        assert isPalindrome("")
        assert isPalindrome(1)
        assert isPalindrome("1")
        assert isPalindrome(33)
        assert isPalindrome("33")
        assert isPalindrome(382283)
        assert isPalindrome("Hello!olleH")
        assert isPalindrome(9999999999)

class BiggestPalindromeBadInput(unittest.TestCase):
    def test_positive_arguments(self):
        self.assertRaises(ValueError, biggestPalindromeFromProduct, -5, 5)
        self.assertRaises(ValueError, biggestPalindromeFromProduct, 0, 5)
        self.assertRaises(ValueError, biggestPalindromeFromProduct, -1, 1)
        self.assertRaises(ValueError, biggestPalindromeFromProduct, 0, 1)
        self.assertRaises(ValueError, biggestPalindromeFromProduct, 0, 5)
    
    def test_bad_order(self):
        self.assertRaises(ValueError, biggestPalindromeFromProduct, 34, 2)
        self.assertRaises(ValueError, biggestPalindromeFromProduct, 999, 100)
    
    def test_non_integers(self):
        self.assertRaises(TypeError, biggestPalindromeFromProduct, 100.0, 999)
        self.assertRaises(TypeError, biggestPalindromeFromProduct, 100, 999.0)
        self.assertRaises(TypeError, biggestPalindromeFromProduct, 100.0, 999.0)

class BiggestPalindromeKnownValues(unittest.TestCase):
    def test_known_values(self):
        # Hard to come up with these on the spot. I'll keep it simple.
        self.assertEqual(biggestPalindromeFromProduct(1, 1), 1)
        self.assertEqual(biggestPalindromeFromProduct(1, 5), 9)
        self.assertEqual(biggestPalindromeFromProduct(4, 8), 0)
        self.assertEqual(biggestPalindromeFromProduct(10, 99), 9009)
        self.assertEqual(biggestPalindromeFromProduct(10, 12), 121)
        self.assertEqual(biggestPalindromeFromProduct(1, 10), 9)
        self.assertEqual(biggestPalindromeFromProduct(1, 20), 19*17)
