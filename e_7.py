#!/usr/bin/env python 
"""
#---
 Julien Lengrand-Lambert
 Created on : Wed Jan 11 14:42:54 CET 2012

 DESCRIPTION : Solves problem 7 of Project Euler
 By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
 that the 6th prime is 13.
 What is the 10 001st prime number? 
#---
""" 
def prime_list(value):
    """
    Returns the value of the 10001st prime number
    """
    prime_list = [2] 
    curr_val = 3
    ptr = False
    while( len(prime_list) < value):
        for primes in prime_list:
            if (curr_val % primes == 0):
                ptr = True # multiple of at least one value
        if not ptr:
            prime_list.append(curr_val)

        curr_val +=1
        ptr = False

    return prime_list[-1]

if __name__ == '__main__':
    val = 10001
    print "Answer : %d " % (prime_list(val))
