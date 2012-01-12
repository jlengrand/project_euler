#!/usr/bin/env python 
"""
#---
 Julien Lengrand-Lambert
 Created on : Wed Jan 11 14:42:54 CET 2012

 DESCRIPTION : Solves problem 6 of Project Euler
 Find the difference between the sum of the squares of the first one hundred 
 natural numbers and the square of the sum.
#---
""" 
def diff_sum_squares(value):
    """
    Returns the difference between the sum of the squares of the first one 
    hundred natural numbers and the square of the sum.
    """
    return squares_sum(value) - sum_squares(value)

def sum_squares(value):
    """
    Returns the sum of the square of elements from 1 to value    
    """
    vals = range(1, value + 1)
    return sum([pow(val, 2) for val in vals])    

def squares_sum(value):
    """
    Returns the square of the sum of elements from 1 to value
    """    
    return pow(sum(range(1, value + 1)), 2)

if __name__ == '__main__':
    val = 100
    print "Answer : %d " % (diff_sum_squares(val))
