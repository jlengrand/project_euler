#!/usr/bin/env python
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : Thu Jan 19 10:12:06 CET 2012
 #
 # DESCRIPTION : Solves problem 27 of Project Euler
 A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

 Euler published the remarkable quadratic formula:
 n^2 + n + 41
 It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
 Considering quadratics of the form:
 n^2 + an + b, where |a| = 1000 and |b| = 1000
 where |n| is the modulus/absolute value of n
 e.g. |11| = 11 and |4| = 4

 Find the product of the coefficients, a and b, 
 for the quadratic expression that produces the maximum number of 
 primes for consecutive values of n, starting with n = 0.
 ##---
 # TODO : enhance with memoization? 
 """
 
def is_prime(value):
    """
    Returns True or False depending whether value is prime or not. 
    """
    start = 2
    while (start <= value / 2):
        if value % start == 0 :
            return False
        else : 
            start += 1
    return True

def quad_fun(a, b, n):
    """
    Returns the result of the Euler quadratic function:
    n^2 + a*n + b
    """
    return (pow(n, 2) + a * n + b)
    
def prime_series(a_range, b_range):
    """
    Returns the product of a and b for the quad_fun that produces the max number of primes; 
    a_range, b_range being the ranges for a and b
    """    
    max = 0
    max_prod = 0
    
    a_curr = 0
    for a in a_range:
        a_curr += 1
        print "%d/%d" %(a_curr, len(a_range))
        for b in b_range:
            
            n = 0
            value = quad_fun(a, b, n)
            while is_prime(abs(value)):
                n += 1
                value = quad_fun(a, b, n)

            # checking if current serie if the best we got : 
            if n > max:
                max = n
                max_prod = a * b
                
    return max_prod
    
if __name__ == '__main__' :
    a_range = range(-999, 1000)
    b_range = range(-999, 1000)
    
    print "Answer is : %d"  % (prime_series(a_range, b_range))
    raw_input()