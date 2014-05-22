#!/usr/bin/env python
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 47 of Project Euler
The first two consecutive numbers to have two distinct prime factors are:

14 = 2*7
15 = 3*5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
'''
import pickle

# list of primes up to one million.
plist = pickle.load(open("primes_list.dup", "rb"))


def is_prime(val):
    """
    Returns True if the number is prime
    """
    return (val in plist)

def consecutive_primes(num):
    """
    Returns the first of the first num consecutive primes.
    """


if __name__ == '__main__':
    print 1
    #print "Answer : %d " % (last_ten())