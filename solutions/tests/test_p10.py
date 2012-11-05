# test_p10.py
#
# Unit tests for Project Euler problem 10
#
# Note that I only test the 

from p10 import *
import unittest

class GetPrimesBelowKnownValues(unittest.TestCase):
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
        
        for i in range(len(knownPrimes)):
            for method in (1,2):
                self.assertEqual(getPrimesBelow(knownPrimes[i] + 1, method),
                            knownPrimes[0:i + 1])
    
    def test_small_values(self):
        for method in (1,2):
            self.assertEqual(getPrimesBelow(0, method), [])
            self.assertEqual(getPrimesBelow(1, method), [])
            self.assertEqual(getPrimesBelow(2, method), [])
    
    def test_float_values(self):
        for method in (1,2):
            self.assertEqual(getPrimesBelow(2.5, method), [2])
            self.assertEqual(getPrimesBelow(3.5, method), [2, 3])
            self.assertEqual(getPrimesBelow(4.5, method), [2, 3])
            self.assertEqual(getPrimesBelow(11.1, method), [2, 3, 5, 7, 11])

class GetPrimesBelowBadInput(unittest.TestCase):
    def test_n_negative(self):
        for method in (1,2):
            self.assertRaises(ValueError, getPrimesBelow, -3, method)
            self.assertRaises(ValueError, getPrimesBelow, -2, method)
            self.assertRaises(ValueError, getPrimesBelow, -1, method)
       
    def test_bad_method_argument(self):
        self.assertRaises(ArgumentError, getPrimesBelow, 10, 0)
        self.assertRaises(ArgumentError, getPrimesBelow, 10, 3)
        self.assertRaises(ArgumentError, getPrimesBelow, 10, -1)
