# p12.py
#
# Solution to Project Euler problem 12
#
#

# ALGORITHM
# Two convenient functions are defined. One of the functions produces the nth
# triangle number using a very simple algorithm. A list of triangle numbers is
# also stored for later use. Another function calculates all of the divisors
# (including 1) of a given number by brute-force. (Another option would be to
# use the prime factors in a clever way.) Each of these functionsare designed
# to be able to be used in other solutions. The actual algorithm is rather
# straight-forward: each triangle number starting from 1 is calculated and its
# factor list computed. The first triangle number whose number of factors
# exceeds 500 is the answer.

from solutionTimer import start, stop
from math import sqrt

triangle_numbers = [1, 3] # Will be populated with [1, 3, 6, 10, 15, ...]
def get_nth_triangle_number(n):
    '''get_nth_triangle_number(n) -> int
    
    Returns the nth triangle number.
    
    >>> get_nth_triangle_number(1)
    1
    >>> get_nth_triangle_number(2)
    3
    >>> get_nth_triangle_number(3)
    6
    >>> get_nth_triangle_number(4)
    10
    '''
    
    # Error checking
    if not isinstance(n, int):
        raise TypeError, 'Argument n must be an integer.'
    if not n >= 1:
        raise ValueError, 'Argument n must be positive.'
    
    desired_index = n - 1
    
    # Check if number has already been calculated
    if n <= len(triangle_numbers):
        return triangle_numbers[desired_index]
    
    while n >= len(triangle_numbers):
        # This is an equivalent recursive-like definition of the triangle
        # numbers:
        new_num = 2*triangle_numbers[-1] - triangle_numbers[-2] + 1
        triangle_numbers.append(new_num)
    
    return triangle_numbers[desired_index]

def factor_list(n):
    '''factor_list(n) -> list
    
    Returns a list of the factors of n.
    
    >>> factor_list(7)
    [1, 7]
    >>> factor_list(16)
    [1, 2, 4, 8, 16]
    '''
    
    # Error checking
    if not isinstance(n, int):
        raise TypeError, 'Argument n must be an integer'
    if not n >= 1:
        raise ValueError, 'Argument n must 1 or greater.'
    
    # Special cases for which int(sqrt(n)) < 2
    if n == 1:
        return [1]
    
    f_list = [1, n]
    
    for f in range(2, int(sqrt(n) + 1)):
        if n % f == 0: # is f a factor of n?
            f_list.append(f)
            if not n/f in f_list: # Is n/f a NEW factor of n?
                f_list.append(n/f)
    
    return sorted(f_list)
    
if __name__ == '__main__':
    start()
    n = 1
    while True:
        tri_num = get_nth_triangle_number(n)
        tri_num_factor_list = factor_list(tri_num)
        if len(tri_num_factor_list) > 500:
            print 'The answer to problem 12 is', tri_num
            break
        n += 1
    stop()