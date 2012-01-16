#!/usr/bin/env python 
"""
 ##---
 # jlengrand
 #Created on : Mon Jan 16 10:02:28 CET 2012
 #
 # DESCRIPTION : Solves problem 13 of Project Euler
 Work out the first ten digits of the sum of the following one-hundred 50-digit numbers. 
 (gris is saved into e_13.data)
 ##---
"""
def ten_dig_sum(filename):
    """
    Returns the first 10 digits of the sum of all numbers in filename.
    """
    return int(str(sum(load_data(filename)))[0:10])

def load_data(filename):
    """
    Loads the data from a file into a table
    """
    file = open(filename, "r")
    data = []
    for line in file :
        data.append(int(line))
    file.close()        
    return data

if __name__ == '__main__':
    #data = ten_dig_sum("e_13.data")
    print "Answer : %d" % (ten_dig_sum("e_13.data"))
