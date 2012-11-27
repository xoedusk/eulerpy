# test_p18.py
#
# Unit tests for Project Euler problem 18

from p18 import *
import unittest

class ExtremeTrianglePathTest(unittest.TestCase):
    def test_known_values(self):
        tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        self.assertEqual(extreme_triangle_path(tri,
                                                    extreme='max',
                                                    operation='add'),
                         23)
