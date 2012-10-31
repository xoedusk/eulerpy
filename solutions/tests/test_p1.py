# test_p1.py
#
# Unit tests for Project Euler, problem 1

import p1
import unittest

class P1UnitTests(unittest.TestCase):
    '''Test cases for p1.py'''
    def test_negativeArguments(self):
        '''Arguments should be positive.'''
        self.assertRaises(ValueError, p1.sumOfMultiples, 999, -3, 5)
        self.assertRaises(ValueError, p1.sumOfMultiples, -999, 3, 5)
        self.assertRaises(ValueError, p1.sumOfMultiples, 999, 3, -5)

    def test_factorsTooBig(self):
        '''One factor should be greater than maxNumber.'''
        self.assertRaises(ValueError, p1.sumOfMultiples, 18, 20, 36)
        self.assertRaises(ValueError, p1.sumOfMultiples, 200, 201, 202)

    def test_wrongType(self):
        '''Only integers are accepted is parameters.'''
        self.assertRaises(TypeError, p1.sumOfMultiples, '999', 3, 5)
        self.assertRaises(TypeError, p1.sumOfMultiples, 999, '3', 5)
        self.assertRaises(TypeError, p1.sumOfMultiples, 999, 3, '5')
        self.assertRaises(TypeError, p1.sumOfMultiples, [999], 3, 5)
        self.assertRaises(TypeError, p1.sumOfMultiples, 999, [3], 5)
        self.assertRaises(TypeError, p1.sumOfMultiples, 999, 3, [5])

    def test_wrongNumberOfArguments(self):
        '''Exactly 3 arguments are allowed'''
        # These exceptions are automatically raised by Python
        self.assertRaises(TypeError, p1.sumOfMultiples, 999, 3)
        self.assertRaises(TypeError, p1.sumOfMultiples, 999)
        self.assertRaises(TypeError, p1.sumOfMultiples)
        self.assertRaises(TypeError, p1.sumOfMultiples, 999, 3, 5, 5)

    def test_knownValues(self):
        '''Known values'''
        self.assertEqual(p1.sumOfMultiples(10, 2, 3), 2 + 3 + 4 + 6 + 8 + 9 + 10)
        self.assertEqual(p1.sumOfMultiples(10, 10, 20), 10)
        self.assertEqual(p1.sumOfMultiples(10, 100, 1), sum(range(1,10+1)))
        self.assertEqual(p1.sumOfMultiples(1, 1, 1), 1)
        self.assertEqual(p1.sumOfMultiples(15, 15, 15), 15)
        self.assertEqual(p1.sumOfMultiples(17, 3, 11), sum(range(3, 17+1, 3)) +
            sum(range(11, 17+1, 11))) # No need to subtract 3*11 multiples

    def test_factor_argument_order_does_not_matter(self):
        self.assertEqual(p1.sumOfMultiples(999, 3, 5), p1.sumOfMultiples(999, 5, 3))

if __name__ == '__main__':
    unittest.main()
