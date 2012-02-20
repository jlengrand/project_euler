#!/usr/bin/env python 
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 53 of Project Euler
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n! / r!(n - r)! ,where r <= n, n! = n * (n - 1) * ... * 3 * 2 * 1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <=  n <= 100, are greater than one-million?
''' 
from utils.memoize import memoize

@memoize
def fact(value):
    """
    Returns value! 
    """
    if value == 0:
        return 1
    return value * fact(value - 1)      

def comb(n, r):
    """
    Returns nCr = n! / r!(n - r)!,where r <= n
    """
    if r > n :
        raise ValueError("n should be >= r !")
    else:
        return (fact(n) / (fact(r) * fact(n - r)))

def upper_comb(max_n, val):
    """
    Returns the number of values of nCr, for 1 <=  n <= max_n that are greater than value?
    """
    nb = 0
    for ns in range(1, max_n + 1):
        for nr in range(1, ns + 1):
            if comb(ns, nr) > val:
                nb += 1
    
    return nb

if __name__ == '__main__':
    print "Answer : %d " % (upper_comb(100, 1000000))