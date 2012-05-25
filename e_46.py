#!/usr/bin/env python 
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 46 of Project Euler
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


NOTE : a composite number is a not prime number
''' 
import pickle

plist = pickle.load(open("primes_list.dup", "rb"))

def is_prime(val):
    """
    Returns True if the number is prime
    """
    return (val in plist)

def gold_fun(prime, val):
    """
    Golbach function
    """
    return prime + 2 * pow(val, 2)

def search_match(val):
    """
    Returns true if val can be written as the sum of a prime and twice a square 
    """
    pval = 0
    prime = plist[0]
    while prime < val :
        curr = 1
        comp = gold_fun(prime, curr)
        while(comp < val):
            curr += 1
            comp = gold_fun(prime, curr)
        if comp == val :
            return True
        
        pval +=1
        prime = plist[pval]
    
    return False

def goldbach():
    """
    Returns the smallest odd composite number that cannot be written as prime + 2*square
    """
    curr = 3
    gold = True
    while(gold):
        curr += 2
        if not(is_prime(curr)) : # can count two by two
            gold = search_match(curr)
    return curr

if __name__ == '__main__':
    print "Answer : %d " % (goldbach())