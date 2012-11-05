# solutionTimer.py
#
# Convenient functions for timing how long some operation takes
#
# USAGE:
# from solutionTimer import start, stop
# start()
# myOperation()
# stop()

from time import time

startTime = 0

def start():
    '''start() -> None
    
    The start() function begins the timer'''
    
    global startTime
    startTime = time()

def stop():
    '''stop() prints a string containing the time difference from start()'''
    stopTime = time()
    totalTime = stopTime - startTime
    print "Operation took %.3f seconds." % totalTime


