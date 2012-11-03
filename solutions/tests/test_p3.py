# test_p3.py
#
# Unit test for Project Euler, problem 3

import unittest
from p3 import *

class PrimeFactorsBadInput(unittest.TestCase):
    def test_only_accepts_integers(self):
        '''Only integers are accepted'''
        self.assertRaises(TypeError, primeFactors, 18.5)
        self.assertRaises(TypeError, primeFactors, "18")
        self.assertRaises(TypeError, primeFactors, [18])
        self.assertRaises(TypeError, primeFactors, (18,))
        self.assertRaises(TypeError, primeFactors, {1: 18})
    
    def test_must_be_2_or_greater(self):
        '''number must be 2 or greater'''
        self.assertRaises(ValueError, primeFactors, -3)
        self.assertRaises(ValueError, primeFactors, -2)
        self.assertRaises(ValueError, primeFactors, -1)
        self.assertRaises(ValueError, primeFactors, 0)
    
class PrimeFactorsKnownValues(unittest.TestCase):
    def test_prime_number_input(self):
        '''behaves well when input is prime number'''
        self.assertEqual(primeFactors(1), [1])
        self.assertEqual(primeFactors(2), [2])
        self.assertEqual(primeFactors(3), [3])
        self.assertEqual(primeFactors(5), [5])
        self.assertEqual(primeFactors(7), [7])
        self.assertEqual(primeFactors(11), [11])
        self.assertEqual(primeFactors(13), [13])
        self.assertEqual(primeFactors(17), [17])
        self.assertEqual(primeFactors(19), [19])
        self.assertEqual(primeFactors(23), [23])
        self.assertEqual(primeFactors(29), [29])
        self.assertEqual(primeFactors(31), [31])
        self.assertEqual(primeFactors(37), [37])
        self.assertEqual(primeFactors(41), [41])
        self.assertEqual(primeFactors(43), [43])
        self.assertEqual(primeFactors(47), [47])
        self.assertEqual(primeFactors(53), [53])
        self.assertEqual(primeFactors(59), [59])
        self.assertEqual(primeFactors(61), [61])
        self.assertEqual(primeFactors(67), [67])
        self.assertEqual(primeFactors(71), [71])
        self.assertEqual(primeFactors(73), [73])
        self.assertEqual(primeFactors(79), [79])
        self.assertEqual(primeFactors(83), [83])
        self.assertEqual(primeFactors(97), [97])
        self.assertEqual(primeFactors(101), [101])
        self.assertEqual(primeFactors(103), [103])
        self.assertEqual(primeFactors(107), [107])
        self.assertEqual(primeFactors(109), [109])
        self.assertEqual(primeFactors(113), [113])
        self.assertEqual(primeFactors(127), [127])
        # Skipped a few
        self.assertEqual(primeFactors(541), [541])
    
    def test_known_composites(self):
        self.assertEqual(primeFactors(4), [2, 2])
        self.assertEqual(primeFactors(6), [2, 3])
        self.assertEqual(primeFactors(8), [2]*3)
        self.assertEqual(primeFactors(9), [3, 3])
        self.assertEqual(primeFactors(10), [2, 5])
        self.assertEqual(primeFactors(12), [2, 2, 3])
        self.assertEqual(primeFactors(14), [2, 7])
        self.assertEqual(primeFactors(15), [3, 5])
        self.assertEqual(primeFactors(16), [2, 2, 2, 2])
        self.assertEqual(primeFactors(18), [2, 3, 3])
        self.assertEqual(primeFactors(20), [2, 2, 5])
        self.assertEqual(primeFactors(22), [2, 11])
        self.assertEqual(primeFactors(24), [2, 2, 2, 3])
        self.assertEqual(primeFactors(25), [5, 5])
        self.assertEqual(primeFactors(26), [2, 13])
        self.assertEqual(primeFactors(27), [3, 3, 3])
        self.assertEqual(primeFactors(28), [2, 2, 7])
        self.assertEqual(primeFactors(30), [2, 3, 5])
        self.assertEqual(primeFactors(360), [2, 2, 2, 3, 3, 5])
        self.assertEqual(primeFactors(1000), [2, 2, 2, 5, 5, 5])
        self.assertEqual(primeFactors(1024), [2]*10)
        self.assertEqual(primeFactors(1025), [5, 5, 41])
