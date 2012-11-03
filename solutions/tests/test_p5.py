# test_p?.py
#
# Unit tests for Project Euler problem ?

from p5 import *
import unittest

class LCMFRKnownValues(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(lowestCommonMultipleFromRange(1, 1), 1)
        self.assertEqual(lowestCommonMultipleFromRange(1, 2), 2)
        self.assertEqual(lowestCommonMultipleFromRange(1, 3), 2*3)
        self.assertEqual(lowestCommonMultipleFromRange(1, 4), 2*3*2)
        self.assertEqual(lowestCommonMultipleFromRange(1, 5), 2*3*2*5)
        self.assertEqual(lowestCommonMultipleFromRange(1, 6), 2*3*2*5)
        self.assertEqual(lowestCommonMultipleFromRange(1, 7), 420)
        self.assertEqual(lowestCommonMultipleFromRange(1, 8), 840)
        self.assertEqual(lowestCommonMultipleFromRange(1, 9), 2520)
        self.assertEqual(lowestCommonMultipleFromRange(1, 10), 2520)
        self.assertEqual(lowestCommonMultipleFromRange(1, 11), 27720)
        self.assertEqual(lowestCommonMultipleFromRange(2, 10), 2520)
        self.assertEqual(lowestCommonMultipleFromRange(3, 7), 3*2*2*5*7)
        self.assertEqual(lowestCommonMultipleFromRange(7, 12), 7*2*2*2*3*3*5*11)
        self.assertEqual(lowestCommonMultipleFromRange(7, 7), 7)
        self.assertEqual(lowestCommonMultipleFromRange(20, 20), 20)
    
class LCMFRBadInput(unittest.TestCase):
    def test_integers_only(self):
        self.assertRaises(TypeError, lowestCommonMultipleFromRange, 1.0, 7)
        self.assertRaises(TypeError, lowestCommonMultipleFromRange, 1, 7.0)
        self.assertRaises(TypeError, lowestCommonMultipleFromRange, 7.0, 12.0)
        self.assertRaises(TypeError, lowestCommonMultipleFromRange, 1.0, 7)
        self.assertRaises(TypeError, lowestCommonMultipleFromRange, "1", 7)
    
    def test_min_max_order(self):
        self.assertRaises(ValueError, lowestCommonMultipleFromRange, 7, 1)
        self.assertRaises(ValueError, lowestCommonMultipleFromRange, 15, 7)
        self.assertRaises(ValueError, lowestCommonMultipleFromRange, 4, 3)
        self.assertRaises(ValueError, lowestCommonMultipleFromRange, 70, 5)
    
    def test_below_1(self):
        self.assertRaises(ValueError, lowestCommonMultipleFromRange, 0, 7)
        self.assertRaises(ValueError, lowestCommonMultipleFromRange, -1, 7)
        self.assertRaises(ValueError, lowestCommonMultipleFromRange, -2, 7)
        self.assertRaises(ValueError, lowestCommonMultipleFromRange, 0, 1)
        self.assertRaises(ValueError, lowestCommonMultipleFromRange, -1, 0)
