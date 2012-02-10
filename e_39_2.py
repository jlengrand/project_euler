#!/usr/bin/env python 
'''
Created on 8 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 39 of Project Euler
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?

This code tends to use classes to find the solution
''' 
class Triangle:
    def __init__(self, a, b, c):
        # c is set as the hypothenuse
        sides = self.set_sides(a, b, c)
        self.a = sides[0]
        self.b = sides[1]
        self.c = sides[2]
    
    def __eq__(self, tri):
        if (self.a == tri.a and self.b == tri.b and self.b == tri.b):
            return True
        else:
            return False

    def set_sides(self, a, b, c):
        """Sets the sides of the Triangle so that c is the largest"""
        return sorted([a, b, c])
    
    def perimeter(self):
        """Returns the perimeter of the Triangle"""
        return self.a + self.b + self.c

    def is_rect(self):
        """Returns True is the Triangle is rectangle"""
        return ( self.a**2 + self.b**2 == self.c**2)


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
                tri = Triangle(a, b, c)
                if tri.is_rect():
                    if is_present(tri, sols):
                        pass
                    else:
                        sols.append(tri)
                        nb_sol += 1
        
        if nb_sol > max_sol:
            max_sol = nb_sol
            max_p = p
            
    return max_p

def is_present(tri, sols):
    """
    Returns True if solution is already in the list
    """
    for sol in sols:
        if sol == tri:
            return True
    return False

if __name__ == '__main__':
    # less ugly solution!
    print "Answer : %d " % (per_tri(1000))
