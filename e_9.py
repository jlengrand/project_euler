#!/usr/bin/env python 
"""
 ##---
 # jlengrand
 #Created on : Fri Jan 13 10:49:29 CET 2012
 #
 # DESCRIPTION : Solves problem 9 of Project Euler
 A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

 a^2 + b^2 = c^2
 For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

 There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 Find the product abc.
 ##---
"""
def pythagorean_triplet(value):
    """
    Returns the product of the Pythagoren triplet for which in addition 
    a + b + c = value 
    """
    pyth_list = pyth_possibilities(value)
    for pyth in pyth_list:
            if is_pyth_triplet(pyth):
                return pyth[0] * pyth[1] * pyth[2]
    return 0

def pyth_possibilities(value):
    """
    Creates a list of all triplets wich sum is equal to value
    FIXME = Is there a way to avoid redundancies? 
    """
    out_list = []
    for j in range(1, value - 1):
        for k in range(1, value - 1):
            out_list.append([j, k, value - j - k])
    return out_list            

def is_pyth_triplet(suite):
    """
    Returns true if the suite contains a pythagorean triplet, false otherwise
    """
    return pow(suite[0], 2) + pow(suite[1], 2) == pow(suite[2], 2)

if __name__ == '__main__':
    val = 1000
    print "Answer : %d" % (pythagorean_triplet(val))
