# p16.py
#
# Solution to Project Euler problem 16
#
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2**1000?

# ALGORITHM
# Not too much to explain here. Convert the number to a string, the string to
# a list of numbers, and then sum the elements of the list.
#
# No unit tests supplied

if __name__ == '__main__':
    print 'Problem 16 ->', sum([int(n) for n in str(2**1000)])