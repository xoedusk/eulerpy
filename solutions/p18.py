# p18.py
#
# Solution to Project Euler problem 18
#
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#
#    3
#   7 4
#  2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
#                             75
#                           95  64
#                         17  47  82
#                       18  35  87  10
#                     20  04  82  47  65
#                   19  01  23  75  03  34
#                 88  02  77  73  07  63  67
#               99  65  04  28  06  16  70  92
#             41  41  26  56  83  40  80  70  33
#           41  48  72  33  47  32  37  16  94  29
#         53  71  44  65  25  43  91  52  97  51  14
#       70  11  33  28  77  73  17  78  39  68  17  57
#     91  71  52  38  17  14  91  43  58  50  27  29  48
#   63  66  04  68  89  53  67  30  73  16  69  87  40  31
# 04  62  98  27  23  09  70  98  73  93  38  53  60  04  23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by
# trying every route. However, Problem 67, is the same challenge with a
# triangle containing one-hundred rows; it cannot be solved by brute force, and
# requires a clever method! ;o)

# ALGORITHM
# My solution does NOT use a brute-force approach, but a 'clever' one. Here is
# the basic idea: Suppose you were located at the second-to-last row at the
# second element, (66). The choice of which element 'below' to go to is
# obvious - it's the larger of the two below it. This can be done for each
# element in the second row. Now replace each element in the second row by the
# sum of it and the bigger of the two element below it. Repeat the process for
# the third row, etc. At the very end, we already have the sum!
#
# The actual algorithm I implemented below differs only in that the PATH
# through the triangle is remembered by storing all the pointers. In addition,
# my algorithm allows to find both the greatest and least of either addition or
# multiplication.

from solutionTimer import start, stop

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def greater(a, b):
    return a > b

def less(a, b):
    return a < b

def extreme_triangle_path(raw_triangle, extreme = 'max', operation = 'add'):
    '''Returns either the min or max sum or product path from the top
    to the bottom of triangle.'''
    
    if extreme == 'max':
        compare = greater
    elif extreme == 'min':
        compare = less
    else:
        raise ValueError, 'Argument extreme must be either "max" or "min".'
    
    if operation == 'add':
        op = add
    elif operation == 'multiply':
        op = multiply
    else:
        raise ValueError, 'Argument operation must be either "add" or "multiply".'

    triangle = raw_triangle[:] # We'll modify triangle in-place.
    for row in range(len(triangle) - 2, -1, -1): # Go in reverse. Need indices
        for col in range(len(triangle[row])):
            if compare(triangle[row + 1][col], triangle[row + 1][col + 1]):
                triangle[row][col] = op(triangle[row][col], triangle[row + 1][col])
            else:
                triangle[row][col] = op(triangle[row][col], triangle[row + 1][col + 1])
        print triangle[row][0]
    
    return triangle[0][0]

if __name__ == '__main__':
    tri = [
        [75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], \
        [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], \
        [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], \
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], \
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], \
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], \
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], \
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], \
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
    start()
    print 'Problem 18 ->', extreme_triangle_path(tri)
    stop()