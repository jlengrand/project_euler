#!/usr/bin/env python 
'''
Created on 7 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 30 of Project Euler
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 24 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
def find_limit(power):
    """
    Returns the max number of digits we have to loop through to find the solution, for a given power
    """
    nb_digits = 2
    max_num = 9**power * nb_digits 
    
    while len(str(max_num)) >= nb_digits:
        nb_digits += 1
        
    return nb_digits - 1
    
def digsum(num, power):
    """
    Returns the sum of power of digits of num
    ex : digsum(123, 4) = 1**4 + 2**4 + 3**4
    """
    val = 0
    for el in str(num):
        val += int(el) ** power
    
    return val
    
def sum_power(power):
    """
    Finds the sum of all the numbers that can be written as the sum of power powers of their digits.
    """
    max_dig = find_limit(power)
    max_val = 9**power * max_dig
    print "Max dig is : %d" %(max_dig)
    sump = 0
    
    cpt = 2
    while cpt <= max_val:        
        if cpt ==  digsum(cpt, power):
            sump += cpt
        
        cpt +=1

    return sump

if __name__ == '__main__':
    # The major problem in there is to find the upper limit.  
    print "Answer : %d " % (sum_power(5))
