#!/usr/bin/env python 
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 31 of Project Euler
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 2^6972593 - 1.
it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p - 1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433 * 2^7830457 + 1.

Find the last ten digits of this prime number.
''' 
def last_ten():
    """
    Returns the last ten digits of  28433 * 2^7830457 + 1
    """
    val = 28433 * pow(2, 7830457) + 1
    return str(val)[-10:]

if __name__ == '__main__':
    #print "Answer : %d " % (last_ten())
    print  pow(2, 7830457)
