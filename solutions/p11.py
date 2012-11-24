# p11.py
#
# Solution to Project Euler problem 11
#
# In the 20x20 grid below, four numbers along a diagonal line have been marked
# in red.
#
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10(26)38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95(63)94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17(78)78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35(14)00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
# The product of these numbers is 26*63*78*14 = 1,788,696.
#
# What is the greatest product of four adjacent numbers in any direction (up,
# down, left, right, or diagonally) in the 20x20 grid?

# ALGORITHM
# Brute force, here. A different function deals with each of vertical, horiz,
# diag DR, and diag DL. These functions compute the product of factors,
# returning the max product it finds. In the end, the global max is printed.
# A few convenient matrix functions are defined here for use in future Euler
# problems.

from solutionTimer import start, stop

class Matrix(object):
    def __init__(self, data):
        # Is data a list?
        if not isinstance(data, list) and not isinstance(data, tuple):
            raise TypeError, 'Argument of Matrix instance must a nested list/'\
                'tuple.'
        
        for row in data:
            # Is each row a list?
            if not isinstance(row, list) and not isinstance(row, tuple):
                raise TypeError, 'Argument of Matrix instance must be a '\
                    'nested list/tuple'
            
            # Is each row the same length?
            if len(row) != len(data[0]):
                raise Error, 'All rows of matrix must be same length.'
            
            #Is each element an int?
            for elem in row:
                if not isinstance(elem, int):
                    raise TypeError, 'Elements of Matrix must be int'
        
        # Get length of first row to compare to other rows
        cols1stRow = len(data[0])
            
        self.__data = data # used internally
        
        self.rows = [[data[r][c] for c in range(len(data[0]))] for r in range(len(data))] # force data into list
        
        self.cols = [[self.rows[r][c] for r in range(len(self.rows))] for c in range(len(self.rows[0]))]
        
    def numCols(self):
        return len(self.cols)
    
    def numRows(self):
        return len(self.rows)
    

def rawTextFileMatrixToInts(rawData):
    rawData = rawData.readlines()
    rawData = [line.rstrip('\n') for line in rawData]
    rawData = [line.split() for line in rawData]
    data = []
    for line in rawData:
        newIntLine = []
        for elem in line:
            newIntLine.append(int(elem))
        data.append(newIntLine)
    
    return data

def getMaxProduct(matrix, numAdjacent,
                  vertical=True, horizontal=True, diagDR=True, diagDL=True):
    '''getMaxProduct(matrix, numAdjacent) -> int
    
    Returns the maximum product of numAdjacent adjacent factors in matrix.
    By default, checks vertical, horizontal, diagDR, and diagDL directions.
    These can be turned off using vertical=False, DiagDR=False, etc. as
    arguments.'''
    
    # Some error checking
    if not isinstance(matrix, Matrix):
        raise TypeError, 'matrix argument must be of type Matrix.'
    if not vertical and not horizontal and not diagDR and not diagDL:
        raise Exception, 'At least one of the four directions must be set to True.'
    if not isinstance(numAdjacent, int):
        raise TypeError, 'numAdjacent argument must be an integer'
    if not numAdjacent >= 1:
        raise Exception, 'numAdjacent argument must be at least 1'
    if numAdjacent > matrix.numCols() and numAdjacent > matrix.numRows():
        raise Exception, 'numAdjacent is too large for the supplied matrix.'
    
    maxProduct = 0 # Assume only working with positive numbers
    
    if vertical:
        if numAdjacent > matrix.numRows():
            raise Exception, 'numAdjacent is too large for the vertical product.'
        maxProduct = max(maxProduct, maxVerticalProduct(matrix, numAdjacent))
    if horizontal:
        if numAdjacent > matrix.numCols():
            raise Exception, 'numAdjacent is too large for the horizontal product.'
        maxProduct = max(maxProduct, maxHorizontalProduct(matrix, numAdjacent))
    if diagDR:
        if numAdjacent > matrix.numCols() or numAdjacent > matrix.numRows():
            raise Exception, 'numAdjacent is too large for the diagDR product.'
        maxProduct = max(maxProduct, maxDiagDRProduct(matrix, numAdjacent))
    if diagDL:
        if numAdjacent > matrix.numCols() or numAdjacent > matrix.numRows():
            raise Exception, 'numAdjacent is too large for the diagDL product.'
        maxProduct = max(maxProduct, maxDiagDLProduct(matrix, numAdjacent))
    
    return maxProduct
    

def maxHorizontalProduct(matrix, numAdjacent):
    _maxProduct = 0
    for r in matrix.rows: # Run over each row in the matrix
        for idx in range(len(r)): # Go over each element; will need index
            if idx > len(r) - numAdjacent + 1: # Too close to end of row?
                break
            p = 1
            for elem in r[idx:idx + numAdjacent]:
                p *= elem
            _maxProduct = max(_maxProduct, p)
    
    return _maxProduct

def maxVerticalProduct(matrix, numAdjacent):
    # Basically a copy of _maxHorizontalProduct
    _maxProduct = 0
    for c in matrix.cols:
        for idx in range(len(c)):
            if idx > len(c) - numAdjacent + 1:
                break
            p = 1
            for elem in c[idx: idx + numAdjacent]:
                p *= elem
            _maxProduct = max(_maxProduct, p)
    
    return _maxProduct


def maxDiagDRProduct(matrix, numAdjacent):
    _maxProduct = 0
    for r_idx in range(matrix.numRows()): # Run through all rows; need index
        if r_idx > matrix.numRows() - (numAdjacent): # Too close to bottom?
            break
        for c_idx in range(matrix.numCols()): # Run horizontally through rows
            if c_idx > matrix.numCols() - (numAdjacent): # Too close to col end?
                break
            p = 1 # Reset product to 1 so that "p *= ..." can be used
            for i in range(numAdjacent):
                p *= matrix.rows[r_idx + i][c_idx + i]
            _maxProduct = max(_maxProduct, p)
    
    return _maxProduct

def maxDiagDLProduct(matrix, numAdjacent):
    _maxProduct = 0
    for r_idx in range(matrix.numRows()): # Run through all rows; need index
        if r_idx > matrix.numRows() - (numAdjacent): # Too close to bottom?
            break
        for c_idx in range(numAdjacent - 1, matrix.numCols()):
            p = 1
            for i in range(numAdjacent):
                p *= matrix.rows[r_idx + i][c_idx - i]
            _maxProduct = max(_maxProduct, p)
    
    return _maxProduct
            

def numCols(matrix):
    return len(matrix)

def numRows(matrix):
    return len(matrix)

if __name__ == '__main__':
    # Get data into a convenient form
    data = open('data/p11.txt', 'r')
    data = rawTextFileMatrixToInts(data)
    data = Matrix(data)
    
    start()
    print 'The answer to problem 11 is', getMaxProduct(data, 4)
    stop()
    
        
    