# test_p7.py
#
# Unit tests for Project Euler problem 7

from p7 import *
import unittest

class GetNthPrimeKnownValues(unittest.TestCase):
    def test_known_values(self):
        knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                       53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
                       109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                       173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                       233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
                       293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                       367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
                       433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
                       499, 503, 509, 521, 523, 541]
        i = 1
        for p in knownPrimes:
            for method in (1, 2):
                self.assertEqual(getNthPrime(i, method), p)
            i += 1
    
class GetNthPrimeBadInput(unittest.TestCase):
    def test_non_positive_input(self):
        for method in (1, 2):
            self.assertRaises(ValueError, getNthPrime, -2, method)
            self.assertRaises(ValueError, getNthPrime, -1, method)
            self.assertRaises(ValueError, getNthPrime, 0, method)
    
    def test_non_integer_input(self):
        for method in (1, 2):
            self.assertRaises(TypeError, getNthPrime, 1.0, method)
            self.assertRaises(TypeError, getNthPrime, 2.0, method)
            self.assertRaises(TypeError, getNthPrime, 3.0, method)
            self.assertRaises(TypeError, getNthPrime, "1", method)
            self.assertRaises(TypeError, getNthPrime, "2", method)
            self.assertRaises(TypeError, getNthPrime, [2], method)
