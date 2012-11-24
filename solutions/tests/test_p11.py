# test_p11.py
#
# Unit tests for Project Euler problem 11

from p11 import *
import unittest

#
#  0 7 2 4 8
#  8 1 1 2 4
#  9 4 0 9 2
#  5 5 4 9 1
#
#  1 3
#  2 0
#
m = Matrix([[0, 7, 2, 4, 8], [8, 1, 1, 2, 4], [9, 4, 0, 9, 2], [5, 5, 4, 9, 1]])
n = Matrix(((1, 3), (2, 0)))

class MatrixInit(unittest.TestCase):
    def test_bad_type(self):
        self.assertRaises(TypeError, Matrix, [3, 4, 6])
        self.assertRaises(TypeError, Matrix, (3, 5, 0))
        self.assertRaises(TypeError, Matrix, [('4', 5), (9, 12)])
        self.assertRaises(TypeError, Matrix, [[5, 1], [7, [8]]])
    
    def test_bad_length(self):
        self.assertRaises(Exception, Matrix, [[3, 5], [7, 7, 7]])
        self.assertRaises(Exception, Matrix, ((4, 4, 4, 4), (2, 2), (4, 4, 4, 4)))
    
    def test_correct_rows_cols(self):
        m = Matrix([[1, 8], [6, 11], [1, 2], [0, -2]])
        self.assertEqual(m.rows, [[1, 8], [6,11], [1, 2], [0, -2]])
        self.assertEqual(m.cols, [[1, 6, 1, 0], [8, 11, 2, -2]])
        
        m = Matrix( ((1,), (2,), (3,)) )
        self.assertEqual(m.rows, [[1], [2], [3]])
        self.assertEqual(m.cols, [[1, 2, 3]])
    
class MaxProductKnownValues(unittest.TestCase):
    def test_max_vertical_product(self):
        self.assertEqual(maxVerticalProduct(m, 1), 9)
        self.assertEqual(maxVerticalProduct(m, 2), 9*9)
        self.assertEqual(maxVerticalProduct(m, 3), 8*9*5)
        self.assertEqual(maxVerticalProduct(m, 4), 4*2*9*9)
        
        self.assertEqual(maxVerticalProduct(n, 1), 3)
        self.assertEqual(maxVerticalProduct(n, 2), 2)
    
    def test_max_horizontal_product(self):
        self.assertEqual(maxHorizontalProduct(m, 1), 9)
        self.assertEqual(maxHorizontalProduct(m, 2), 9*4)
        self.assertEqual(maxHorizontalProduct(m, 3), 5*4*9)
        self.assertEqual(maxHorizontalProduct(m, 4), 5*5*4*9)
        self.assertEqual(maxHorizontalProduct(m, 5), 5*5*4*9*1)
        
        self.assertEqual(maxHorizontalProduct(n, 1), 3)
        self.assertEqual(maxHorizontalProduct(n, 2), 3)
    
    def test_max_dr_product(self):
        self.assertEqual(maxDiagDRProduct(m, 1), 9)
        self.assertEqual(maxDiagDRProduct(m, 2), 9*5)
        self.assertEqual(maxDiagDRProduct(m, 3), 8*4*4)
        self.assertEqual(maxDiagDRProduct(m, 4), 7*1*9*1)
        
        self.assertEqual(maxDiagDRProduct(n, 1), 3)
        self.assertEqual(maxDiagDRProduct(n, 2), 0)
    
    def test_max_dl_product(self):
        self.assertEqual(maxDiagDLProduct(m, 1), 9)
        self.assertEqual(maxDiagDLProduct(m, 2), 7*8)
        self.assertEqual(maxDiagDLProduct(m, 3), 4*9*4)
        self.assertEqual(maxDiagDLProduct(m, 4), 5*4*1*4)
        
        self.assertEqual(maxDiagDLProduct(n, 1), 3)
        self.assertEqual(maxDiagDLProduct(n, 2), 6)
    
    def test_max_product(self):
        self.assertEqual(getMaxProduct(m, 1), 9)
        self.assertEqual(getMaxProduct(m, 2), 9*9)
        self.assertEqual(getMaxProduct(m, 3), 8*9*5)
        self.assertEqual(getMaxProduct(m, 4), 5*5*4*9)
        self.assertEqual(getMaxProduct(m, 5,
                                       vertical=False,
                                       diagDR=False,
                                       diagDL=False), 5*5*4*9*1)
        
        self.assertEqual(getMaxProduct(n, 1), 3)
        self.assertEqual(getMaxProduct(n, 2), 6)

class MaxProductBadInput(unittest.TestCase):
    def test_numadjacent_bad_value(self):
        self.assertRaises(Exception, getMaxProduct, m, 6)
        self.assertRaises(Exception, getMaxProduct, m, 0)
    def test_numadjacent_wrong_type(self):
        self.assertRaises(TypeError, getMaxProduct, m, '4')
    def test_wrong_matrix_type(self):
        self.assertRaises(TypeError, getMaxProduct, [[1, 2], [3, 4]])
    