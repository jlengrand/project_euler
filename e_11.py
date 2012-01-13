#!/usr/bin/env python 
"""
 ##---
 # jlengrand
 #Created on : Fri Jan 13 15:24:59 CET 2012
 #
 # DESCRIPTION : Solves problem 11 of Project Euler
 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
 What is the sum of the digits of the number 2^1000?
 ##---
"""
def sum_power_2(value):
    """
    Returns the sum of the digits of 2^value
    """
    
    return 1

if __name__ == '__main__':
    print "Answer : %d" % (sum_power_2(1000))
