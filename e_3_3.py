#!/usr/bin/env python 
"""
#---
 Julien Lengrand-Lambert
 Created on : Wed Jan 11 14:42:54 CET 2012

 DESCRIPTION : Solves problem 3 of Project Euler
 The prime factors of 13195 are 5, 7, 13 and 29.
 What is the largest prime factor of the number 600851475143 ?
#---
""" 
def largest_prime_factor(value):
    """
    Returns the largest prime factor of value
    """
    curr_prime = 2 # first prime 
    
    while curr_prime < value:
        while value % curr_prime == 0:
            value /= curr_prime
        
        curr_prime += 1 

    return value

if __name__ == '__main__':
    val = 600851475143 
    print "Answer : %d " % (largest_prime_factor(val))