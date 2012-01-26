#!/usr/bin/env python
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : Thu Jan 19 10:12:06 CET 2012
 #
 # DESCRIPTION : Solves problem 23 of Project Euler
 A perfect number is a number for which the sum of its proper divisors is 
 exactly equal to the number. For example, the sum of the proper divisors of 28
 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

 A number n is called deficient if the sum of its proper divisors is less than 
 n and it is called abundant if this sum exceeds n.

 As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
 number that can be written as the sum of two abundant numbers is 24. 
 By mathematical analysis, it can be shown that all integers greater than 28123
 can be written as the sum of two abundant numbers. However, this upper limit
 cannot be reduced any further by analysis even though it is known that the 
 greatest number that cannot be expressed as the sum of two abundant numbers
 is less than this limit.

 Find the sum of all the positive integers which cannot be written as the sum 
 of two abundant numbers.
 
 
 Hum : Once again, solution is wayyy to long ! (about 20 minuts)
 Starts slowly, but gets faster as soon as abundants numbers are big.
 ##---
"""
max_sum_abundant = 28123

def sum_abundant_numbers():
    """
    Returns the sum of all the positive integers that cannot be written as the sum of
    two abundant numbers.
    """
    global max_sum_abundant
    
    numbers = range(max_sum_abundant + 1)
    abundants = [i for i in numbers if is_abundant(i)]
    
    print "starting to count"
    
    for ii in abundants:
        print "%d /%d" %(ii, max_sum_abundant)
        for jj in abundants:
            curr_sum = ii + jj
            if curr_sum <= max_sum_abundant: #We don't want to go over the max
                try: # ok because all numbers are unique
                    numbers.remove(curr_sum)
                except ValueError: # if not exists, already removed
                    pass
                     
    return sum(numbers)

def get_divisors(value):
    """
    Returns the list of proper divisors of value
    """
    div = []
    for val in range(1, value ):
        if (value % val == 0): 
            div.append(val)
    return div

def is_abundant(value):
    """
    Returns True or False depending whether a number is abundant or not. 
    """
    return sum(get_divisors(value)) > value
    
if __name__ == '__main__' :
    print "Answer is : %d" %( sum_abundant_numbers())
    raw_input() # USed to keep Windows terminal open
