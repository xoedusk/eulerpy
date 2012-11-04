# p6.py
#
# Solution to Project Euler problem 6
#
#

# ALGORITHM
# Calculate the square of sums and sum of squares in two separate functions.
# the __main__ part just calls a function that subtracts the two .

def sumOfSquares(listOfValues):
    sum = 0
    for i in listOfValues:
        sum += i**2
    return sum

def squareOfSum(listOfValues):
    sum = 0
    for i in listOfValues:
        sum += i
    square = sum**2
    return square

def diffSquareSumSumSquare(listOfValues):
    squareSum = squareOfSum(listOfValues)
    sumSquare = sumOfSquares(listOfValues)
    return squareSum - sumSquare

if __name__ == '__main__':
    p6Range = range(1, 100 + 1)
    print "The answer to problem 6 is %d" % diffSquareSumSumSquare(p6Range)