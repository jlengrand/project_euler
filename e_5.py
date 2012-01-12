#!/usr/bin/env python 
"""
#---
 Julien Lengrand-Lambert
 Created on : Wed Jan 11 14:42:54 CET 2012

 DESCRIPTION : Solves problem 5 of Project Euler
 2520 is the smallest number that can be divided by each of the numbers from 1 
 to 10 without any remainder.
 What is the smallest positive number that is evenly divisible by all of the 
 numbers from 1 to 20? 
#---
""" 
def divisible_by_all():
    """
    Returns the smallest number divisible by 1 to 20
    """
    dividers = range(1, 20)[::-1] # in reverse order
    max_div = dividers[0] + 1
    ptr = 2
    inc = 0

    while 1:
        val = max_div * ptr
        # if divisible by all dividers
        for divider in dividers:
            if (val % divider != 0):
                break
            inc += 1

        if inc == len(dividers):                
            return val          
        else :
            inc = 0 
        ptr += 1 

if __name__ == '__main__':
    print "Answer : %d " % (divisible_by_all())
