#!/usr/bin/env python
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : Thu Jan 19 10:12:06 CET 2012
 #
 # DESCRIPTION : Puts the list of all primes below one million in a file. 
 Seeing the number of problems using primes, this could be useful
 ##---
 """ 
import pickle

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
 
if __name__ == '__main__' :
    if 0: # creating file
        plist = prime_list(1000000)
        # dumping into primes_list.dump
        pickle.dump(plist, open("primes_list.dup", "wb"))
    else: # reading and using file
        plist = pickle.load(open("primes_list.dup", "rb"))
        print plist[0:100]
        raw_input()
    print "Done!"
