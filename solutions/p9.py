# p9.py
#
# Solution to Project Euler problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# a**2 + b**2 == c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# ALGORITHM
# Square roots can be tricky, because they tend to return floats, even when
# the answer is a pure integer. In addition, 3 == 2.999999999999999999999999
# can evaluate to True. Therefore, my algorithm avoids square roots and
# comparisions of quantities that might be close. Nothing fancy for the actual
# algorithm; basically just brute force.

def isPythagoreanTriplet(a, b, c):
    return a**2 + b**2 - c**2 == 0

if __name__ == '__main__':
    fixed = 1000
    foundTriplet = False
    # The order and ranges of the these 3 for loops ensures 1 < a < b < c
    for c in range(fixed - 3, 3 - 1, -1):
        for b in range(c - 1, 2 - 1, -1):
            a = fixed - b - c
            if a < 1:
                break
            if isPythagoreanTriplet(a, b, c):
                foundTriplet = True
                print "The answer to problem 9 is %s" % (a*b*c)
                break
        if foundTriplet:
            break
