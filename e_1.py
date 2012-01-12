#!/usr/bin/env python 
"""
#---
 Julien Lengrand-Lambert
 Created on : Wed Jan 11 14:32:18 CET 2012

 DESCRIPTION : Soves problem 1 of Project Euler
 If we list all the natural numbers below 10 that are multiples of 3 or 5
 we get 3, 5, 6 and 9. The sum of these multiples is 23.
 Find the sum of all the multiples of 3 or 5 below 1000.
#---

"""
def natural_sum(max_value, start_value=1):
    """
    Sums up all natural values multiple to 3 or 5 between max_value and 
    start_value
    No error checks performed
    """
    nat_sum = 0
    curr_value = start_value
    while (curr_value < max_value):
        if ((curr_value % 3 == 0) or (curr_value % 5 == 0) ):
            nat_sum += curr_value            
        curr_value += 1
    
    return nat_sum


if __name__ == '__main__':
    print "Answer : %d" % (natural_sum(1000))
