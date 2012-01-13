#!/usr/bin/env python 
"""
 ##---
 # jlengrand
 #Created on : Fri Jan 13 11:42:09 CET 2012
 #
 # DESCRIPTION : Solves problem 10 of Project Euler
 The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 Find the sum of all the primes below two million.
 ##---
"""
def sum_primes(value):
    """
    Returns the sum of prime number below value
    """
    prime_list = [2] 
    curr_val = 3
    ptr = False
    while( curr_val < value):
        for primes in prime_list:
            if (curr_val % primes == 0):
                ptr = True # multiple of at least one value
        if not ptr:
            prime_list.append(curr_val)
            print "%d%% / %d" % (((prime_list[-1] / float(value)) * 100), prime_list[-1])

        curr_val +=1
        ptr = False
    
    return sum(prime_list)

if __name__ == '__main__':
    print "Answer : %d" % (sum_primes(2000000))
