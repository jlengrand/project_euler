#!/usr/bin/env python 
"""
#---
 jlengrand
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
    max_match = pow(value, 0.5) + 1
    curr_prime = 2
    rest = value
    fin_prime = curr_prime

    while (curr_prime <= max_match or curr_prime < rest):
        if (rest % curr_prime == 0):
            fin_prime = curr_prime 
        while (rest % curr_prime == 0):
            rest = rest / curr_prime
        curr_prime += 1
        if (curr_prime % 1000000 == 0):
            print "%d / %d / %d" % (curr_prime, rest, max_match)
    return fin_prime

if __name__ == '__main__':
    val = 600851475143 
    print "Answer : %d " % (largest_prime_factor(val))
