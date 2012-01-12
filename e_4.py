#!/usr/bin/env python 
"""
#---
 Julien Lengrand-Lambert
 Created on : Wed Jan 11 14:42:54 CET 2012

 DESCRIPTION : Solves problem 4 of Project Euler
 A palindromic number reads the same both ways. The largest palindrome made 
 from the product of two 2-digit numbers is 9009 = 91  99.
 Find the largest palindrome made from the product of two 3-digit numbers.
#---
""" 
def largest_palindrom():
    """
    Returns the largest palindrom made from the product of two 3-digits number
    """
    three_digits = range(100, 1000)
    largest = 0

    for digit_1 in three_digits:
        for digit_2 in three_digits:
            val = digit_1 * digit_2
            if is_palindrom(val):
                if largest < val:
                    largest = val
    return largest

def is_palindrom(number):
    """
    returns True if a number is a palindrom, False otherwise
    """
    return str(number)[::-1] == str(number)

if __name__ == '__main__':
    print "Answer : %d " % (largest_palindrom())
