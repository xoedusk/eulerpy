# p1.py
#
# Project Euler
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# ALGORITHM
# Run through all numbers from 1 to 1000, checking if each one is a multiple
# of 3 or 5. If it is, add it to a list. At the end, add up all of the
# elements of the list.

def sumOfMultiples(maxNumber, factor1, factor2):
    # Begin error checking
    for i in (maxNumber, factor1, factor2):
        if not isinstance(i, int):
            raise TypeError, "All parameters must be an integers."
        if i < 1:
            raise ValueError, "All parameters must be positive."
    if factor1 > maxNumber and factor2 > maxNumber:
        raise ValueError, "Both factor1 and factor2 arguments must be less "\
            "than maxNumber."
    
    # Begin algorithm
    multiples = [x for x in range(1, maxNumber + 1)
                 if x % factor1 == 0 or x % factor2 == 0]
    return sum(multiples)

if __name__ == "__main__":
    print "The answer to problem 1 is %d" % sumOfMultiples(999, 3, 5)
