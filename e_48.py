#!/usr/bin/env python 
"""
 ##---
 # jlengrand
 #Created on : Mon Jan 16 15:47:00 CET 2012
 #
 # DESCRIPTION : Solves problem 48 of Project Euler
 The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
 Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
 ##---
"""
def sum_pow(max_val):
    """
    Returns the last 10 digits of 1^1 + ... + max_val^max_val
    """
    summ = 0
    for j in range(1, max_val + 1):
        summ += pow(j, j)
    
    return int(str(summ)[-10:])

if __name__ == '__main__':
    print "Answer : %d" % (sum_pow(1000))
