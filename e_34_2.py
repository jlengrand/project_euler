#!/usr/bin/env python 
'''
Created on 8 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 34 of Project Euler
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
''' 
import timeit
from utils.memoize import memoize

def find_limit():
    """
    Returns the max number of digits we have to loop through to find the solution
    """
    nb_digits = 2
    max_num = fact(9) * nb_digits 
    
    while len(str(max_num)) >= nb_digits:
        nb_digits += 1
        
    return nb_digits - 1

@memoize
def fact(value):
    """
    Returns value! 
    """
    if value == 0:
        return 1
    return value * fact(value - 1)      

def digsum(num):
    """
    Returns the sum of factorial of digits of num
    ex : digsum(123, 4) = fact(1) + fact(2) + fact(3)
    """
    val = 0
    for el in str(num):
        val += fact(int(el))
    
    return val

def sum_fact2():
    """
    Finds the sum of all the numbers that can be written as the sum of the factorial of their digits.
    """
    max_dig = find_limit()
    max_val = fact(9) * max_dig
    print "Max dig is : %d" %(max_dig)
    sumf = 0    
    
    cpt = 3
    while cpt <= max_val:    
        if cpt ==  digsum(cpt):
            sumf += cpt
        
        cpt +=1

    return sumf

if __name__ == '__main__':
    # The major problem in there is to find the upper limit.
    t2 = timeit.Timer("sum_fact2()", "from __main__ import sum_fact2")
    print t2.timeit(1)
