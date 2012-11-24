# p14.py
#
# Solution to Project Euler problem 14
#
# The following iterative sequence is defined for the set of positive integers:
# n  n/2 (n is even)
# n  3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following
# sequence:
# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?

# ALGORITHM
# This uses an iterative algorithm, rather than a recursive one.

from solutionTimer import start, stop

collatz_dict = {1: None} # Will contain individual mappings: 2 -> 1, 5 -> 16
collatz_dict_list = {1: [1]} # Will contain mappings to complete lists

def collatz(n, method = 2):
    '''collatz(n, method=2) -> list
    
    Returns a list containing the Collatz sequence, starting at n and ending
    at 1. The 'method' may be either 1 or 2. Method 1 uses a 'minimalist'
    key-value pair algorithm: each number gets assigned as a key in a
    dictionary, with the corresponding value being the next number in the
    sequence. Method 2 also uses a key-value pair data-structure, but the
    value is the entire Collatz sequence associated with the key. Method 2
    is faster than method 1.
    
    >>> collatz(1)
    [1]
    >>> collatz(17, method=1)
    [17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    '''
    if not isinstance(n, int):
        raise TypeError, 'Argument n must be a positive integer.'
    if not n >= 1:
        raise ValueError, 'Argument n must be a positive integer.'
    if not (method==1 or method==2):
        raise ValueError, 'Argument method must be either 1 or 2'
    
    if method == 1:
        return _collatz1(n)
    elif method == 2:
        return _collatz2(n)

def _collatz1(n):
    elem = n # This is the next element in the sequence
    while not elem in collatz_dict:
        _next = _next_element(elem)
        collatz_dict[elem] = _next
        elem = _next
    
    # Now build the sequence that will be returned
    seq = []
    elem = n
    while collatz_dict[elem]: # Not that collatz_dict[1] == None
        seq.append(elem)
        elem = collatz_dict[elem]
    seq.append(1)
    
    return seq

def _collatz2(n):
    if n in collatz_dict_list:
        return collatz_dict_list[n]
    else: # Must make new sequence
        seq = []
        elem = n
        while elem not in collatz_dict_list: # Will always be run >= once
            seq.append(elem)
            elem = _next_element(elem)
        seq.extend(collatz_dict_list[elem])
        collatz_dict_list[n] = seq
        return seq

def _next_element(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1
    
if __name__ == '__main__':
    start()
    max_len = 1
    answer = 1
    for n in range(1, int(1e6)):
        if len(collatz(n, method=2)) > max_len:
            max_len = len(collatz(n))
            answer = n
    print 'The answer to problem 14 is', answer
    stop()
