#!/usr/bin/env python 
"""
 ##---
 # jlengrand
 #Created on : Fri Jan 13 15:41:12 CET 2012
 #
 # DESCRIPTION : Solves problem 20 of Project Euler
 n! means n  (n  1)  ...  3  2  1
 For example, 10! = 10  9  ...  3  2  1 = 3628800,
 and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
 Find the sum of the digits in the number 100! 
 ##---
"""
def sum_fact(value):
    """
    Returns the sum of digits in value!
    """
    
    return 1

if __name__ == '__main__':
    print "Answer : %d" % (sum_fact)
