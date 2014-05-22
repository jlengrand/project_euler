#!/usr/bin/env python
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 49 of Project Euler
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
import pickle

# list of primes up to one million.
plist = pickle.load(open("primes_list.dup", "rb"))

def fourLengthPrime():
    """
    Returns the list of all prime numbers of length 4
    """
    return(val for val in plist if len(str(val)) == 4)

def isPrime(val):
    """
    Returns True if the number is prime
    """
    return (val in plist)

def all_permutations(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]
            for m in all_permutations(part):
                temp.append(seq[k:k+1] + m)
        return temp

def getPrimesPermutations(primes, length):
    """
    Returns all the lists of primes that are permutations from one another,
    and of size at least 3.
    """
    if True:
    #for prime in primes :
        prime = primes.next()
        perms = [int(val) for val in all_permutations(str(prime))]
        print perms

def findPrimePerms(prime):
    """
    Returns all the list of primes that are permutations from prime
    """
    perms = [int(val) for val in all_permutations(str(prime)) if (isPrime(int(val)) and len(str(int(val))) == 4)]
    res = list(set(perms)) # rermoves duplicates
    if len(res) > 2:
        return res

if __name__ == '__main__':
    primes = fourLengthPrime()
    print findPrimePerms(primes.next())
    print findPrimePerms(primes.next())
    print findPrimePerms(primes.next())
    print findPrimePerms(primes.next())
    #print "Answer : %d " % (last_ten())