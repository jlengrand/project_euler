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
    max_len = 1
    seed = 1
    for val in range(1, max_value + 1):
        curr_len = seq_len(val)
        if curr_len > max_len:
            max_len = curr_len
            seed = val

    return seed

def seq_len(value):
    """
    Returns the sequence length for a given value
    """
    val = value
    seq = [val]
    
    while val != 1:
        val = sequence(val)
        seq.append(val)
    return len(seq)

def is_even(value):
    """
    Returns true if the given value is even, false otherwise
    """
    return (value % 2 == 0)

def sequence(value):
    """
    Returns value / 2 if value is even, 3 * n + 1 otherwise.
    """
    if is_even(value):
        return value / 2
    else:
        return 3 * value + 1        

if __name__ == '__main__':
    print "Answer : %d" % (longest_chain(1000000))
