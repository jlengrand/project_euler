#!/usr/bin/env python
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : Thu Jan 19 10:12:06 CET 2012
 #
 # DESCRIPTION : Solves problem 35 of Project Euler
 The number, 197, is called a circular prime because all rotations of the digits: 
 197, 971, and 719, are themselves prime.
 There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
 How many circular primes are there below one million?
 ##---
 """
import pickle

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
    
def prime_list(max_val):
    """
    Returns a list of all primes below max_val
    """
    plist = []
    cur = 2
    while (cur < max_val):
        if (cur % 1000) == 0:    
            print "%d/%d" % (cur, max_val)
            
        if (is_prime(cur)):
            plist.append(cur)
        cur += 1
        
    return plist

def contains_even(val):
    """
    Returns True f val contains an even number (ex : 998)
    """
    return (str(2) in str(val) or str(4) in str(val)  or str(6) in str(val) or str(8) in str(val))
    
def divisible_by_3(val):
    """
    Returns True of val is divisible by 3 (ex : 12)
    """    
    temp = sum([int(p) for p in str(val)])
    if len(str(temp)) > 1:
        divisible_by_3(temp)
    else:
        return ((temp % 3) == 0)

def check_easy_out(plist):
    """
    Returns the number of circular primes below max_val
    
    TODO : offer cleaner method
    """
    pred = list(plist)
    for p in plist:
        if p > 11: # my filter does not work for values under 10
            # ugly method
            #if (contains_even(p) or divisible_by_3(p)):
            if (contains_even(p)): # no prime divisible by 3 . . . 
                # could also test for 3 and 9 
                pred.remove(p)    
    return pred
 
def perm_primes(max_val):
    """
    Returns the number of circular primes below max_val
    """
    circulars = 0
    circl = []    
    
    #plist = prime_list(max_val)
    plist = pickle.load(open("primes_list.dup", "rb"))
    p_reduced = check_easy_out(plist) 
    
    print len(plist)
    print len(p_reduced)

    print p_reduced

    checks_list = [1] * len(p_reduced) # all primes to be tested
 
    for ii in range(len(p_reduced)):
        if (ii % 99 == 0):
            print "%d/%d" % ( ii + 1, len(p_reduced))

        if checks_list[ii]: # if prime still to be checked
            prime = p_reduced[ii]
            perms = all_permutations(str(prime)) # finds all permutations

            # counts how many permutations are in prime list given one prime
            p_cpt = 0
            for perm in perms:
                if int(perm) in p_reduced:
                    p_cpt += 1

            # if prime is circular
            if p_cpt == len(perms):                  
                # updating checks_list
                for perm in perms:
                    if not(int(perm) in circl): # avoiding duplicates
                        circulars += 1
                        circl.append(int(perm))
                    checks_list[p_reduced.index(int(perm))] = 0
                    
            else:
                checks_list[ii] = 0
    
    return circulars, circl  

 
if __name__ == '__main__' :
    #perm_primes(1000000)
    answer, plist = perm_primes(1000000)
    print "Answer is : %d"  % (answer)