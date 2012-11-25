# test_p15.py
#
# Unit tests for Project Euler problem 15

from p15 import *
import unittest
from math import factorial

class NumWaysThroughGridTest(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(num_ways_through_grid(0, 1), 1)
        self.assertEqual(num_ways_through_grid(1, 0), 1)
        self.assertEqual(num_ways_through_grid(1, 1), 2)
        self.assertEqual(num_ways_through_grid(1, 2), 3)
        self.assertEqual(num_ways_through_grid(2, 1), 3)
        self.assertEqual(num_ways_through_grid(2, 2), 6)
    
    def test_grid_too_small(self):
        for x in range(-2, 0):
            for y in range(-2, 0):
                self.assertRaises(ValueError, num_ways_through_grid, x, y)
    
    def test_wrong_type(self):
        self.assertRaises(TypeError, num_ways_through_grid, '5', 5)
        self.assertRaises(TypeError, num_ways_through_grid, 5.0, 5)



