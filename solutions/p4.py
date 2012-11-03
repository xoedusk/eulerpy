# p4.py
#
# Project Euler, problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91*99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

# ALGORITHM
# Just brute force here. Go through all of the products of 3 digit numbers,
# check if it's bigger than the current biggest palindrome. If it is, check
# if it itself is a palindrome, and if so, replace the biggest palindrome.
# Some time is saved if the remaning products in a given loop will be less
# than the biggest palindrome.

def isPalindrome(n):
    '''Takes any single argument. Returns True or False, depending on whether
    it is a palindrome in its string-state.'''
    n = str(n)
    reversed = n[::-1]
    return n == reversed

def biggestPalindromeFromProduct(min, max):
    '''Returns biggest numeric palindrome between the numbers min and
    max. Returns 0 if there are no palindromes.'''
    if min > max:
        raise ValueError, "min must be equal to or less than max."
    if max < 1 or min < 1:
        raise ValueError, "Arguments must be 1 or greater"
    biggestPalindrome = 0
    rangeOfProducts = range(max, min - 1, -1)
    for i in rangeOfProducts:
        if i**2 < biggestPalindrome:
            break
        for j in range(i, min - 1, -1): # Do N**2/2, not N**2
            product = i*j
            if product <= biggestPalindrome:
                break
            if product > biggestPalindrome: # Comparing ints is fast
                if isPalindrome(product): # ...so this is second.
                    biggestPalindrome = product
    return biggestPalindrome

if __name__ == '__main__':
    print "The largest palindrome from products between "\
        "%d and %d is %d" % (100, 999, biggestPalindromeFromProduct(100, 999))