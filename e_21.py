#!/usr/bin/env python 
"""
 ##---
 # jlengrand
 #Created on : Mon Jan 16 16:22:29 CET 2012
 #
 # DESCRIPTION : Solves problem 21 of Project Euler
 Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
 If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

 For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

 Evaluate the sum of all the amicable numbers under 10000. 
 ##---
"""
def amicable_numbers(max_val):
    """
    Returns the sum of amicable numbers under max_val
    """
    am_list = []
    for val in range(1, max_val):
        am = sum_divisors(val)
        if am != val and sum_divisors(am) == val : 
            am_list.append(val)
    
    return sum(am_list)

def sum_divisors(value):
    """
    Returns the sum of the list of proper divisors of value
    """
    div = []
    for val in range(1, value ):
        if (value % val == 0): 
            div.append(val)
    return sum(div)

if __name__ == '__main__':
    print "Answer : %d" % (amicable_numbers(10000))
