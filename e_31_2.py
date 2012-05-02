#!/usr/bin/env python 
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 31 of Project Euler
In England the currency is made up of pound and pence, p, and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
It is possible to make L2 in the following way:

1 * L1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p
How many different ways can L2 be made using any number of coins?

This problem is known as the coin change problem.
''' 
S = [1, 2, 5, 10, 20, 50, 100, 200] # set of coins

def coin_change(n, m):
    """
    Solves the coin change problem for a given set of coins and a desired value.
    Recursive way
    """
    # initial conditions
    if n == 0 :
        return 1
    if n < 0:
        return 0
    if m <= 0 and n >= 1 :
        return 1
    # either a coin is not in the solution, and can be removed from the set
    part1 = coin_change(n, m - 1)
    # or it is part of it, and the final wanted value can be reduced (n - value of the coin)
    part2 = coin_change(n - S[m], m)
    return  part1 + part2

if __name__ == '__main__':
    answer = coin_change(200, len(S) - 1)
    print "Answer is : %d"  % (answer)
    