# p?.py
#
# Solution to Project Euler problem ?
#
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

# ALGORITHM
# Get a list of the prime factors of each number in the specified range. Add
# the factors into a dictionary keyed by factor and valued by number of times
# the factor appeared. Dictionary only needs to be updated if it is missing
# some of the prime factors.

from p3 import primeFactors

def lowestCommonMultipleFromRange(min, max):
    '''Returns the lowest common multiple of all integers from min to max,
    inclusive'''
    
    if not isinstance(min, int) or not isinstance(max, int):
        raise TypeError, "Parameters must be integers"
    if min > max:
        raise ValueError, "min must be lower than max"
    if min < 1:
        raise ValueError, "parameters must be positive"
    
    primeDict = {}
    numRange = range(min, max + 1)
    lcm = 1
    
    for n in numRange:
        factors = primeFactors(n)
        for p in factors: # This is a bit wasteful for numbers like a*b**n, n>>1
            count = factors.count(p)
            try:
                if primeDict[p] < count:
                    primeDict[p] = count
            except KeyError:
                primeDict[p] = count
    
    # Now multiply all the items in primeDict
    for p,n in primeDict.items():
        lcm *= p**n
    
    return lcm

if __name__ == '__main__':
    print "The answer to problem 5 is %d" % lowestCommonMultipleFromRange(1, 20)