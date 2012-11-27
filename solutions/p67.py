# p67.py
#
# Solution to Project Euler problem 67
#
#

# ALGORITHM

from p18 import extreme_triangle_path

if __name__ == '__main__':
    data = open('data/p67.txt', 'r')
    data = [line.rstrip('\n').split() for line in data]
    tri = []
    for row in data:
        new_row = []
        for elem in row:
            new_row.append(int(elem))
        tri.append(new_row)
    
    start()
    print 'Problem 67 ->', extreme_triangle_path(tri)
    stop()