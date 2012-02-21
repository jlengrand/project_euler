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
import timeit

def largest_prime_factor(value):
    """
    Returns the largest prime factor of value
    """
    # max_match = pow(value, 0.5)
    max_match = value / 2
    curr_prime = 2
    rest = value
    primes = []

    while (curr_prime <= max_match):
        if (rest % curr_prime == 0):
            primes.append(curr_prime) 
        while (rest % curr_prime == 0):
            rest = rest / curr_prime
        curr_prime += 1
    return max(primes)

if __name__ == '__main__':
    val = 600851475143 
    #print "Answer : %d " % ()
    t2 = timeit.Timer("largest_prime_factor(%d)" % (val), "from __main__ import largest_prime_factor")
    print t2.timeit(1)