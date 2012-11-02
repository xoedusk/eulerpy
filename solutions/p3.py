# p3.py

# Project Euler
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# ALGORITHM
# Find first factor of number by running from 2 to sqrt(N), until a number p
# is found that divides N evenly. That is the lowest prime. Add it to an array.
# Take the quotient and repeat the process, starting over at 2. At the end,
# take the last element of the p-array. This algorithm is easily implemented
# recursively, but I chose to go the iterative route.

from math import sqrt

def primeFactors(n):
    '''Returns an ascending list of prime factors of parameter n. If n is
    prime, the list only contains n itself (not the list [1, n]).'''
    if not isinstance(n, int):
        raise TypeError, "Only integers are acceptable is input to primeFactors(n)"
    if n < 2:
        raise ValueError, "Parameter must be at least 2."
    
    primeFactorList = [n] # Populate the primeFactor list with number, as it may
                       # itself be prime. If not, it'll be removed.
    newPrimeFound = True # Used to check when to stop searching for a new prime
    while newPrimeFound: # Equality iff no new primes found
        newPrimeFound = False
        factorRange = [2]
        factorRange.extend(range(3, int(sqrt(primeFactorList[-1])) + 1, 2))
        for j in factorRange:
            if primeFactorList[-1] % j == 0 and j != primeFactorList[-1]:
                primeFactorList.insert(-1, j)
                primeFactorList.insert(-1, primeFactorList[-1]/j)
                primeFactorList.pop()
                newPrimeFound = True
                break
    return primeFactorList

if __name__ == '__main__':
    print "The largest prime factor of 600851475143 is "\
        "%d" % primeFactors(600851475143)[-1]
