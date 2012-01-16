#!/usr/bin/env python 
"""
 ##---
 # jlengrand
 #Created on : Mon Jan 16 13:53:07 CET 2012
 #
 # DESCRIPTION : Solves problem 15 of Project Euler
 Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
 How many routes are there through a 20x20 grid?

 This problem is linked with the catalan number.
 To get to the extreme right, 2xn moves have to be performed
 Moves are either R or D. 
 There is the same the same number of R and D in the sequence.
 
 Problem is finally : How many strings of size 2xn are there consisting of nxR and nxD? 
 -> number of ways in which we can choose n positions from 2xn available.
 binomial :
 (2n n) = (2n)! / (n! x n!)
 ##---
"""
def square_grid_path(n):
    """
    Returns the number of paths from top left to bottom right of a 
    nxn grid. 
    """
    return (fact(2*n) / (fact(n) * fact(n)))

def fact(value):
    """
    Returns value!
    """
    if value < 2:
        return value
    else:
        return value * fact(value - 1)        

if __name__ == '__main__':
    print "Answer : %d" % (square_grid_path(20))
