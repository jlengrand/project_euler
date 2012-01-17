#!/usr/bin/env python 
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : Mon Jan 16 15:34:46 CET 2012
 #
 # DESCRIPTION : Solves problem 18 of Project Euler
 By starting at the top of the triangle below and moving to adjacent numbers on
 the row below, the maximum total from top to bottom is 23.
    3
   7 4
  2 4 6
 8 5 9 3
 That is, 3 + 7 + 4 + 9 = 23.

 Find the maximum total from top to bottom of the triangle saved in e_18.data
 ##---
"""
import itertools

def longest_path(filename):
    """
    Returns the maximum total top from bottom of the triangle saved in filename
    """        
    data = load_triangle(filename)

    reference = []
    reference.extend(data)

    values = list(itertools.chain(*data))
    values.sort() # we loose non sorted variable
    sort_val = list(set(values))

    reverse_val = []
    reverse_val.extend(sort_val)
    reverse_val.reverse()

    print sort_val
    print reverse_val
    print reference

    return 1

def load_triangle(filename):
    """
    Returns a list of lists from triangle given in filename
    """
    data = []
    file = open(filename, "r")
    for line in file :
        data.append([int(el) for el in line.split(" " ) ])
    file.close()

    return data

if __name__ == '__main__':
    print "Answer : %d" % (longest_path("e_18.data"))
