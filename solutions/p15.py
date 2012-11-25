# p15.py
#
# Solution to Project Euler problem 15
#
# Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

# How many routes are there through a 20x20 grid?

# ALGORITHM
# This is a very simple problem to do mathematically. One way to interpret
# the view the problem is that, since you MUST go right exactly 20 times and
# you MUST go down exactly 20 times, you are simply trying to find the number
# of unique arrangements of 40 elements, 20 of which are identical to each
# other, and the other 20 elemments are identicaly to each other. The answer
# is (40!)/(20! * 20!), where '!' is the factorial unary operator.

from solutionTimer import start, stop
from math import factorial

def num_ways_through_grid(x, y):
    '''num_ways_through_grid(x, y) -> int
    
    Returns the number of unique paths a point in the upper left corner of an
    x by y grid to a point in the lower right corner.
    
    >>> num_ways_through_grid(2, 2)
    6
    
    '''
    
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError, 'Arguments x and y must be integers.'
    if not ((x >= 0 and y >= 1) or (x >= 1 and y >= 0)):
        raise ValueError, 'Grid too small; must be 0x1, 1x0, or bigger.'
    
    return factorial(x + y) / (factorial(x)*factorial(y))

if __name__ == '__main__':
    start()
    print 'The answer to problem 15 is', num_ways_through_grid(20, 20)
    stop()