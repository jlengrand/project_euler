#!/usr/bin/env python 
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 37 of Project Euler
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
''' 
import pickle

plist = pickle.load(open("primes_list.dup", "rb"))

def is_prime(val):
    """
    Returns True if the number is prime
    """
    return (val in plist)

def trunc_left(val):
    """
    Returns true if the prime number is truncatable from left to right
    """
    if not is_prime(val):
        return False
    if len(str(val)) == 1:
        return True
    else:
        return trunc_left(int(str(val)[1:]))

def trunc_right(val):
    """
    Returns true if the prime number is truncatable from left to right
    """
    if not is_prime(val):
        return False
    if len(str(val)) == 1:
        return True
    else:
        return trunc_right(int(str(val)[:-1]))

def trunc_primes():
    """
    Returns the complete list of primes that are both truncatable from left to right and right to left
    """
    # there we already have to 1 million.
    inplist = list(plist)
    out_list = []

    for p in inplist:
        if p > 11:
            if (trunc_left(p) and trunc_right(p)):
                print "Found one : %d" %(p)
                out_list.append(p)
                
        if len(out_list) > 10 : #already found them all
            return out_list
        
    print "End of the line. Should go higher than one million !"
    return out_list

if __name__ == '__main__':
    # We know that there are only 11 of them. Lets try to find them
    print trunc_primes()
    print "Answer : %d " % (sum(trunc_primes()))