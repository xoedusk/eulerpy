# test_p12.py
#
# Unit tests for Project Euler problem 12

from p12 import *
import unittest

class GetNthTriangleNumber(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(get_nth_triangle_number(1), 1)
        self.assertEqual(get_nth_triangle_number(2), 3)
        self.assertEqual(get_nth_triangle_number(3), 6)
        self.assertEqual(get_nth_triangle_number(4), 10)
        self.assertEqual(get_nth_triangle_number(5), 15)
        self.assertEqual(get_nth_triangle_number(6), 21)
        self.assertEqual(get_nth_triangle_number(7), 28)
        self.assertEqual(get_nth_triangle_number(8), 36)
        self.assertEqual(get_nth_triangle_number(9), 45)
        self.assertEqual(get_nth_triangle_number(10), 55)
        self.assertEqual(get_nth_triangle_number(11), 66)
    
    def test_bad_input(self):
        self.assertRaises(ValueError, get_nth_triangle_number, 0)
        self.assertRaises(TypeError, get_nth_triangle_number, 3.0)
        self.assertRaises(TypeError, get_nth_triangle_number, '3')
        self.assertRaises(ValueError, get_nth_triangle_number, -3)
    
class FactorList(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(factor_list(1), [1])
        self.assertEqual(factor_list(2), [1, 2])
        self.assertEqual(factor_list(3), [1, 3])
        self.assertEqual(factor_list(4), [1, 2, 4])
        self.assertEqual(factor_list(5), [1, 5])
        self.assertEqual(factor_list(6), [1, 2, 3, 6])
        self.assertEqual(factor_list(7), [1, 7])
        self.assertEqual(factor_list(8), [1, 2, 4, 8])
        self.assertEqual(factor_list(9), [1, 3, 9])
        self.assertEqual(factor_list(10), [1, 2, 5, 10])
        self.assertEqual(factor_list(11), [1, 11])
    
    def test_bad_input(self):
        self.assertRaises(ValueError, factor_list, 0)
        self.assertRaises(TypeError, factor_list, 4.0)
        self.assertRaises(TypeError, factor_list, '4')
        self.assertRaises(ValueError, factor_list, -4)
        
        