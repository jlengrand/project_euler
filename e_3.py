#!/usr/bin/env python 
"""
#---
 Advansee
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
        if (curr_prime % 10000 == 0):
            print "%d/%d" % (curr_prime, value)
    return max(primes)

if __name__ == '__main__':
    val = 600851475143 
    print "Answer : %d " % (largest_prime_factor(val))
