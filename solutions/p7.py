# p7.py
#
# Solution to Project Euler problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10001st prime number?

# ALGORITHM
# Two very different algorithms that can both compute the nth prime are coded.
# One of them (algorithm 2) is much faster than the other.
#
# Alorithm 1 (slow)
# This uses an 'incremental' version of the Eratosthenes sieve. The problem
# with the usual Eratosthenes method is that it's really only easily
# implemented up to a certain number; that is, it's good for finding primes
# less than or equal to a given number. Since, in our problem, we have no way
# of knowning what our 'maximum' number is, the sieve method needs modifying.
# One option is to dynamically increase the maximum number in some clever way,
# but this seems less interesting to me than the incremental method, which goes
# as follows:
# Instead of crossing out ALL the multiples up to sqrt(n) for a given prime n,
# only cross out ONE of them, then update this one multiple as we come to
# checking if it is prime or not. For each newly found prime p, the first
# multiple to remember is p**2 (since prior multiples have smaller prime
# factors).
#
# Algorithm 2 (fast)
# This uses a trial division algorithm. It checks if each odd number is
# divisible by any of the known primes. If not, it's appended to the known
# list of primes. 

import time
from math import sqrt

def _getNthPrimeEratosthenes(n): # slow
    '''getNthPrimeEratosthenes(n) -> n
    
    Returns the nth prime number using incremental Eratosthenes sieve method.'''
    
    primesMultiples = {2: 2**2}
    candidate = 3
    
    while len(primesMultiples) < n:
        if candidate in primesMultiples.values(): # candidate is a multiple
            for p,m in primesMultiples.items(): # Need to find all the prime factors
                if candidate == m: # numToCheck a multiple of p
                    primesMultiples[p] += 2*p # += p would be even
        else: # candidate is a prime
            primesMultiples[candidate] = candidate**2
        
        candidate += 2
    
    return max(primesMultiples.keys())

def _getNthPrimeTrialDivision(n): # fast
    '''getNthPrimeTrianDivision(n) -> integer
    
    Returns the nth prime number by using trial division algorithm'''
    primes = [] # Avoid adding 2 to the list of primes for now. This improves
                # the speed by about 10 milliseconds
    candidate = 3
    
    while len(primes) < n - 1: # minus 1 because 2 was not added to prime list
        candidateIsPrime = True
        for p in primes:
            if p > sqrt(candidate):
                break
            if candidate % p == 0: # candidate is not a prime
                candidateIsPrime = False
                break
        if candidateIsPrime:
            primes.append(candidate)
        candidate += 2
        
    primes.insert(0, 2)
    
    return primes[-1]
    
def getNthPrime(n, method=1):
    '''getNthPrime(n, method=1) -> integer
    
    Returns the nth prime number using one of two methods:
    method = 1: use incremental Eratosthenis sieve method
    method = 2: use trial division method'''
    if not isinstance(n, int):
        raise TypeError, "argument must be a positive integer"
    if n < 1:
        raise ValueError, "Argument must be a positive integer"
    
    if method == 1:
        return _getNthPrimeEratosthenes(n)
    elif method == 2:
        return _getNthPrimeTrialDivision(n)
    else:
        raise ValueError, "method argument must be either 1 or 2. See docstring."

if __name__ == '__main__':
    startTime = time.time()
    n = getNthPrime(10001, 2)
    totalTime = time.time() - startTime
    print "The answer to problem 7 is %d" % n
    print "Finished in %.3f seconds" % totalTime