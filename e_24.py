#!/usr/bin/env python
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : Thu Jan 19 10:12:06 CET 2012
 #
 # DESCRIPTION : Solves problem 24 of Project Euler
 A permutation is an ordered arrangement of objects. For example, 3124 is one 
 possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are 
 listed numerically or alphabetically, we call it lexicographic order. 
 The lexicographic permutations of 0, 1 and 2 are:
 012   021   102   120   201   210
 
 What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
 ##---
 """
def lexi_perm(str, num):
    """
    Returns the numst lexicographic permutations of all values in str
    """
    # already sorted by all_permutations!
    return int(all_permutations(str)[num - 1])
 
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
 
if __name__ == '__main__' :
    lexi_perm("012", 1)
    #print "Answer is : %d" %(lexi_perm("0123456789", 1000000))
    raw_input() # USed to keep Windows terminal open
