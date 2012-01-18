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
import copy
import itertools

def longest_path(filename):
    """
    Returns the maximum total top from bottom of the triangle saved in filename
    """        
    # data is the actual triangle
    # rev_data the shortest path modification
    # sort_val a list of unique values of data sorted by ascending order
    # reverse_val the same values, reversed. Will be used to create the second 
    # rectangle
    
    data = load_triangle(filename)

    # creating sort_val
    values = list(itertools.chain(*data))
    values.sort() # we loose non sorted variable
    sort_val = list(set(values))

    # creating reverse_val
    reverse_val = []
    reverse_val.extend(sort_val)
    reverse_val.reverse()

    # creating rev_data
    rev_data = copy.deepcopy(data) # deepcopy because nested list
    for index, item in enumerate(rev_data):
        for s_index, s_item in enumerate(item):
            rev_data[index][s_index] = reverse_val[sort_val.index(s_item)]

    if 0:    
        print"###"
        print sort_val
        print reverse_val
        print "###"
        print data
        print rev_data

    # dikstra here!

    return 1

def shortest_path(data):
    """
    Finds the shortest path to go through data
    """
    
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
