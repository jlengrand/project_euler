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
''' 

def listmul(list1, list2):
    """Multiplies each elements of list1 and list 2 with each other"""
    if len(list1) != len(list2):
        raise ValueError("Lists are supposed to have the same length!")

    else:
        out = []
        for ii in range(len(list1)):
            out.append(list1[ii] * list2[ii])
            
        return out

if __name__ == '__main__':
    
    values = [1, 2, 5, 10, 20, 50, 100, 200]
    goal = 200
    
    max_vals = [goal / val for val in values]
    # we have to solve the equation a * 1 + b * 2 + c * 5 + d * 10 + e * 20 + f * 50 + g *100 + h * 200 = goal
    cur_vals = [0] * len(values)
    
    sols = 0
    for cur_vals[0] in range(max_vals[0] + 1):
        print cur_vals[0]
        for cur_vals[1] in range(max_vals[1] + 1):
            print cur_vals[1]
            for cur_vals[2] in range(max_vals[2] + 1):
                for cur_vals[3] in range(max_vals[3] + 1):
                    for cur_vals[4] in range(max_vals[4] + 1):
                        for cur_vals[5] in range(max_vals[5] + 1):
                            for cur_vals[6] in range(max_vals[6] + 1):
                                for cur_vals[7] in range(max_vals[7] + 1):
                                    if sum(listmul(cur_vals, values)) == goal:
                                        sols += 1
    print sols
    