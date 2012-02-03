#!/usr/bin/env python
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : Thu Jan 19 10:12:06 CET 2012
 #
 # DESCRIPTION : Solves problem 36 of Project Euler
 The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
 Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

 (Please note that the palindromic number, in either base, may not include leading zeros.)
 ##---
 """
    
    
def is_palindrom(number):
    """
    Returns True if a number is a palindrom, False otherwise
    """
    return str(number)[::-1] == str(number)

def dec2strbin(number):
    """
    Returns a string value, corresponding to number expressed in base 2.
    """
    return bin(number)[2:]
    
def sum_palindroms(max):
    """
    Returns the sum, less than max, which are palindromic in both 10 and 2 bases.
    """
    sump = 0
    curr = 0
    while (curr < max):
        if  (is_palindrom(curr) and is_palindrom(dec2strbin(curr))):
            sump += curr
            
        curr += 1
    
    return sump
    
if __name__ == '__main__' :
    print "Answer is : %d"  % (sum_palindroms(1000000))
