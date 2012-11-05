# p10.py
#
# Solution to Project Euler problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# ALGORITHM
# The two possibilities that come to my mind are the Eratosthenes sieve method
# and a trial division method. Both algorithms will be coded. The trial
# division algorithm is largely based on p7.py, and is MUCH faster than my
# implementation of the sieve. Both methods utilize a list of all primes so
# that they can be used in other problems; thus, it is not as fast as
# algorithms that simply return a sum.

from math import sqrt, ceil
from solutionTimer import start, stop

class ArgumentError(Exception): pass

def getPrimesBelow(n, method = 1):
    '''getPrimesBelow(n, method=1) -> integer
    
    Returns a list of all prime numbers less than n using one of two methods:
    method = 1: Eratosthenes sieve
    method = 2: Trial by division'''
    
    if n < 0:
        raise ValueError, "n must be a positive integer"
    elif n <= 2:
        return []
    
    n = int(ceil(n))
    
    if method == 1:
        return _getPrimesBelowEratosthenes(n)
    elif method == 2:
        return _getPrimesBelowTrialDivision(n)
    else:
        raise ArgumentError, "method argument must be either 1 or 2. See "\
            "docstring."

def _getPrimesBelowEratosthenes(n): # slow
    '''_getPrimesBelowTrialDivision(n) -> list
    
    Returns an ascending list of all prime numbers less than n.'''
    candidates = range(3, n, 2)   # candidates contains 3 to n-1, odd numbers
    
    for c in candidates:
        for m in range(3*c, n, 2*c):
            try:
                candidates.remove(m) # Remove all multiples of c
            except ValueError:
                pass
        if c > int(sqrt(n-1)):
            break
    
    candidates.insert(0, 2)
    return candidates

def _getPrimesBelowTrialDivision(n): # fast
    '''_getPrimesBelowTrialDivision(n) -> list
    
    Returns an ascending list of all prime numbers less than n.'''
    primes = [] # Avoid adding 2 to the list of primes for now.
    candidate = 3
    
    while candidate < n:
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
    
    return primes

if __name__ == '__main__':
    start()
    total = sum(getPrimesBelow(2000000, 2))
    stop()
    print "The answer to problem 10 is %d" % total
