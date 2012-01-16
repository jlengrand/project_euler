#!/usr/bin/env python 
"""
 ##---
 # jlengrand
 #Created on : Mon Jan 16 10:22:33 CET 2012
 #
 # DESCRIPTION : Solves problem 14 of Project Euler
 The following iterative sequence is defined for the set of positive integers:

 n -> n/2 (n is even)
 n -> 3n + 1 (n is odd)
 
 Using the rule above and starting with 13, we generate the following sequence:
 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
 It can be seen that this sequence (starting at 13 and finishing at 1) contains 
 10 terms. 
 Although it has not been proved yet (Collatz Problem), it is thought that all 
 starting numbers finish at 1.

 Which starting number, under one million, produces the longest chain?

 NOTE: Once the chain starts the terms are allowed to go above one million. 
 ##---
"""
def longest_chain(max_value):
    """
    Returns the starting number under max_value that produces the longest 
    chain given the sequence.
    """
    
    return 1

if __name__ == '__main__':
    print "Answer : %d" % (longest_chain(1000000))
