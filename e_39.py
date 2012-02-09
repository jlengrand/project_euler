#!/usr/bin/env python 
'''
Created on 8 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 39 of Project Euler
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?
''' 
def per_tri(max_per):
    """
    Returns the maximum number of solutions maximised for a given max value of perimeter.  
    """
    max_sol = 0
    max_p = 0
    for p in range(3, max_per + 1):
        print "%d/%d" %(p, max_per + 1)
        nb_sol = 0
        sols = []
        for a in range(1, p):
            for b in range(1, p - a):
                c = p - a - b
                if is_rect(a, b, c):
                    if is_present([a, b, c], sols):
                        pass
                    else:
                        sols.append([a, b, c])
                        nb_sol += 1
        
        if nb_sol > max_sol:
            max_sol = nb_sol
            max_p = p
            
    return max_p

def is_present(cur_sol, sols):
    """
    Returns True if solution is already in the list
    """
    for sol in sols:
        val = 0
        for side in cur_sol:
            if side in sol:
                val += 1
        
        if val == len(cur_sol):
            return True
    
    return False

def is_rect(a, b, c):
    """
    Returns true if the triangle is rectangle, c being the hypothenuse.
    """
    return (a**2 + b**2 == c**2)

if __name__ == '__main__':
    # really ugly solution!
    print "Answer : %d " % (per_tri(1000))
