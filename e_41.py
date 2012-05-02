#!/usr/bin/env python 
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 41 of Project Euler
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
''' 

val = 123456789 # all numbers to create the biggest pandigital number
def is_prime(value):
    """
    Returns True or False depending whether value is prime or not. 
    """
    start = 2
    while (start <= value / 2):
        if value % start == 0 :
            return False
        else : 
            start += 1
    return True

# I could use a decorator to remove trivial non primes here
def all_permutations(seq):
    """permutates a sequence and returns a list of the permutations"""
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]
            for m in all_permutations(part):
                temp.append(seq[k:k+1] + m)
        return temp

def divisible_by_2(val):
    """
    Returns True if val contains an even number (ex : 998)
    """
    return ((val % 2) == 0)

def divisible_by_5(val):
    """
    Returns True if any circular permutation of val is divisible by  (ex : 907)
    """    
    return (str(5) == str(val)[-1])
    
def divisible_by_3(val):
    """
    Returns True if any circular permutation of val is divisible by 3 (ex : 12)
    """    
    temp = sum([int(p) for p in str(val)])
    if len(str(temp)) > 1:
        divisible_by_3(temp)
    else:
        return ((temp % 3) == 0)

def check_easy_out(pelist):
    """
    Returns the number of circular primes below max_val
    
    TODO : do this while creating all the permutations !
    """
    pred = list(pelist)
    for p in pelist:
        if p > 11: # my filter does not work for values under 10
            if (divisible_by_2(p) or divisible_by_5(p) or divisible_by_3(p)): 
                pred.remove(p)    
    return pred

def biggest_pandigital():
    """
    Returns the biggest pandigital prime number
    """
    for n in range(9): # from 0 to 9 numbers removed of max pand number
        print " n : %d" %(n)
        root = str(val)[:len(str(val)) -n]
        perms = [ int(p) for p in all_permutations(root)]
        perms = check_easy_out(perms)
        perms.sort(reverse=True)
        for p in perms : 
            if is_prime(p):
                return p
        
    return -1 # problem
if __name__ == '__main__':
    print "Answer : %d " % (biggest_pandigital())