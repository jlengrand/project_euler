#!/usr/bin/env python 
"""
 ##---
 # jlengrand
 #Created on : Fri Jan 13 15:59:15 CET 2012
 #
 # DESCRIPTION : Solves problem 11 of Project Euler
 What is the greatest product of four adjacent numbers in any direction 
 (up, down, left, right, or diagonally) in the 20x20 grid? 
 (gris is saved into e_11.data
 ##---
"""
from operator import mul

def great_prod_grid(filename, square_size):
    """
    Returns the greatest product of 4 adjacent numbers in the grid.
    """
    data = load_data(filename)
    great_prod  = 0 
    for j in range(square_size - 3):
        for k in range(square_size - 3):
            # 3 possibilities here
            a = data[j][k:k + 4]
            b = []
            c = []
            for l in range(4):
                b.append(data[j + l][k]) 
                c.append(data[j + l][k + l])
            if j == square_size - 4:
                if k == square_size - 4:
                    print a, b, c                        
            for val in [a, b, c]:
                prod = prod_list(val)
                if prod > great_prod:            
                    great_prod = prod
    return great_prod

def prod_list(data):
    """
    Returns the product of all elements in a list of integers
    """
    return reduce(mul, data)

def load_data(filename):
    """
    Loads the data from a file into a table
    """
    file = open(filename, "r")
    data = []
    for line in file :
        data.append([int(el) for el in line.split( )])
    file.close()        
    return data

if __name__ == '__main__':
    print "Answer : %d" % (great_prod_grid("./e_11.data", 20))
