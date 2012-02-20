#!/usr/bin/env python 
'''
Created on 17 feb. 2012

@author: Julien Lengrand-Lambert
@contact: julien@lengrand.fr
''' 
import timeit
from memoize import memoize
from Memoized import Memoized

def fact1(value):
    """
    Returns value! 
    """
    if value == 0:
        return 1
    return value * fact1(value - 1)      
    
@memoize
def fact2(value):
    """
    Returns value!, using memoization 
    """
    if value == 0:
        return 1
    return value * fact2(value - 1)     

@Memoized
def fact3(value):
    """
    Returns value!, using memoization 
    """
    if value == 0:
        return 1
    return value * fact3(value - 1)   
    
if __name__ == '__main__':
    for i in range(3):
        t1 = timeit.Timer("fact1(150)", "from __main__ import fact1")
        t2 = timeit.Timer("fact2(150)", "from __main__ import fact2")
        t3 = timeit.Timer("fact3(150)", "from __main__ import fact3")
        print t1.timeit(1), t2.timeit(1), t3.timeit(1)