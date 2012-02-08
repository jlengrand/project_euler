#!/usr/bin/env python 
'''
Created on 8 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 28 of Project Euler
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
''' 
def sum_diag(max_lines):
    """
    Returns the sum of both diagonals of the square of max_lines size
    """
    dsum = 1 # sum of diagonals
    cpt = 1 # number of lines processed
    val = 1 # value of the current place in the square
    inc = 0 # the increment between number for one line
    
    while cpt < max_lines:
        cpt += 2
        inc += 2
        
        for corner in range(4):
            val += inc
            dsum += val

    return dsum

if __name__ == '__main__':
    # The major problem in there is to find the logic
    #n = 1 gives 1 
    #n = 3 gives 3, 5, 7, 9 => +2
    #n = 5 gives 13, 17, 21, 25 => +4
    #n = 7 gives 31, 37, 43, 49 => +6
    #n = 9 gives 57, . . .      
    print "Answer : %d " % (sum_diag(1001))
