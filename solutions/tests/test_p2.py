# test_p2.py
#
# Unit tests for p2.py

from p2 import *
import unittest

class fibSequenceUnitTests(unittest.TestCase):
    def test_integer_parameter(self):
        '''fibSequenceBelowValue should only accept integer parameters'''
        self.assertRaises(TypeError, fibSequenceBelowValue, "10")
        self.assertRaises(TypeError, fibSequenceBelowValue, 10.0)
        self.assertRaises(TypeError, fibSequenceBelowValue, [10])
        self.assertRaises(TypeError, fibSequenceBelowValue, (10,))
    
    def test_positive_parameter(self):
        '''fibSequenceBelowValue parameter must be greater than 1'''
        self.assertRaises(NoSequenceElementsBelowGivenParameter,
                          fibSequenceBelowValue, 1)
        self.assertRaises(NoSequenceElementsBelowGivenParameter,
                          fibSequenceBelowValue, 0)
        self.assertRaises(NoSequenceElementsBelowGivenParameter,
                          fibSequenceBelowValue, -1)
        self.assertRaises(NoSequenceElementsBelowGivenParameter,
                          fibSequenceBelowValue, -2)
        self.assertRaises(NoSequenceElementsBelowGivenParameter,
                          fibSequenceBelowValue, -3)
    
    def test_parameter_too_low(self):
        '''fibSequenceBelowValue unable to give sequence when parameter is 1'''
        self.assertRaises(NoSequenceElementsBelowGivenParameter, fibSequenceBelowValue, 1)
    
    def test_known_values(self):
        '''fibSequenceBelowValue should return correct known values'''
        self.assertEqual(fibSequenceBelowValue(2), [1])
        self.assertEqual(fibSequenceBelowValue(3), [1,2])
        self.assertEqual(fibSequenceBelowValue(4), [1, 2, 3])
        self.assertEqual(fibSequenceBelowValue(5), [1, 2, 3])
        self.assertEqual(fibSequenceBelowValue(6), [1, 2, 3, 5])
        self.assertEqual(fibSequenceBelowValue(14), [1, 2, 3, 5, 8, 13])
        self.assertEqual(fibSequenceBelowValue(15), [1, 2, 3, 5, 8, 13])
        self.assertEqual(fibSequenceBelowValue(49), [1, 2, 3, 5, 8, 13, 21, 34])

class sumEvenElementsUnitTests(unittest.TestCase):
    def test_parameter_is_list_of_positive_integers(self):
        '''sumEvenElements requires an iterable of integers'''
        self.assertRaises(TypeError, sumEvenElements, [[1,2,3,4,5,6]])
        self.assertRaises(TypeError, sumEvenElements, [1,2,3,'4',5,6])
        self.assertRaises(TypeError, sumEvenElements, 2)
        self.assertRaises(TypeError, sumEvenElements, [1, 2, [3], 4])
        self.assertRaises(TypeError, sumEvenElements, [1, 2, 3, 4.5])
        self.assertRaises(TypeError, sumEvenElements, [1, 2, -3, 4])
    
    def test_known_values(self):
        '''sumEvenElements returns correct known values'''
        self.assertEqual(sumEvenElements([6, 8, 1, 0, 7 , 1 , 3, 9, 4]),
                         6 + 8 + 4)
        self.assertEqual(sumEvenElements([2, 4, 6]), 2 + 4 + 6)
        self.assertEqual(sumEvenElements([2, 2, 2]), 2 + 2 + 2)
        self.assertEqual(sumEvenElements([10]), 10)
        self.assertEqual(sumEvenElements([1, 3, 5, 7]), 0)
        self.assertEqual(sumEvenElements([0]), 0)
        self.assertEqual(sumEvenElements([0, 2, 3]), 2)
    
    def test_order_doesnt_matter(self):
        self.assertEqual(sumEvenElements([1, 2, 3, 4, 5, 6]), sumEvenElements([6, 5, 4, 3, 2, 1]))
    
    def test_lists_tuples(self):
        '''lists and tuples yield the same value in sumEvenElements'''
        self.assertEqual(sumEvenElements([1, 2, 3, 4, 5]), sumEvenElements((1, 2, 3, 4, 5)))
    

if __name__ == '__main__':
    unittest.main()