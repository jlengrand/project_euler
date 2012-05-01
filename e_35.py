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

def shift(seq, n):
    """
    Shifts a sequence by n rotations
    """
    seq = str(seq)
    return int(seq[n:]+seq[:n])

def all_rotations(seq):
    """
    Returns a list of all possible rotations of a number 
    """
    out = []
    for n in range(len(str(seq))):
        out.append(int(shift(str(seq), n)))

    return out

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
    Returns True if val contains an even number (ex : 998)
    """
    return ((str(2) in str(val)) or (str(4) in str(val))  or (str(6) in str(val)) or (str(8) in str(val)))

def divisible_by_5(val):
    """
    Returns True if any circular permutation of val is divisible by  (ex : 907)
    """    
    return ((str(5) in str(val)) or (str(0) in str(val)))
    
def divisible_by_3(val):
    """
    Returns True if any circular permutation of val is divisible by 3 (ex : 12)
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
            if (contains_even(p) or divisible_by_5(p)): # no prime divisible by 3 . . . 
                pred.remove(p)    
    return pred
 
def perm_primes(max_val):
    """
    Returns the number of circular primes below max_val
    """
    plist = prime_list(max_val)
    #plist = pickle.load(open("primes_list.dup", "rb"))
    p_reduced = check_easy_out(plist) 
    
    p_out = []
    
    print len(plist)
    print len(p_reduced)
    
    print p_reduced
    
    for p in p_reduced:
        perms = all_rotations(p)
        perms = list(set(perms)) # removes duplicates
        perms = [int(p) for p in perms]

        circl = 0
        for pp in perms:
            if pp in p_reduced: # in list of primes
                circl += 1
                
        if circl == len(perms):
            p_out = p_out + perms
            
        circl = 0
           
    p_out = list(set(p_out)) 
    return len(p_out)
 
if __name__ == '__main__' :
    answer = perm_primes(1000000)
    print "Answer is : %d"  % (answer)   