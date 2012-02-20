#!/usr/bin/env python 
'''
Created on 17 feb. 2012

@author: Julien Lengrand-Lambert
@contact: julien@lengrand.fr
''' 
import timeit
from memoize import memoize
from Memoized import Memoized

def fib1(n):
    """Returns the n st value of Fibonnacci list"""
    if n < 2:
        return n
    else:
        return fib1(n-1) + fib1(n - 2)
    
@memoize
def fib2(n):
    """Returns the n st value of Fibonnacci list, using memoization"""
    if n < 2:
        return n
    else:
        return fib2(n-1) + fib2(n - 2)

@Memoized
def fib3(n):
    """Returns the n st value of Fibonnacci list, using memoization"""
    if n < 2:
        return n
    else:
        return fib3(n-1) + fib3(n - 2)
    
if __name__ == '__main__': 
    for i in range(3):
        t1 = timeit.Timer("fib1(20)", "from __main__ import fib1")
        t2 = timeit.Timer("fib2(20)", "from __main__ import fib2")
        t3 = timeit.Timer("fib3(20)", "from __main__ import fib3")
        print t1.timeit(1), t2.timeit(1), t3.timeit(1)    