#!/usr/bin/env python 
"""
 ##---
 # jlengrand
 #Created on : Mon Jan 16 14:01:09 CET 2012
 #
 # DESCRIPTION : Solves problem 25 of Project Euler
 The Fibonacci sequence is defined by the recurrence relation:

 Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
 The 12th term, F12, is the first term to contain three digits.

 What is the first term in the Fibonacci sequence to contain 1000 digits?
 ##---
"""
def fibo_dig_count(count):
    """
    Returns the first term of Fibonacci sequence to contain count digits
    """
    last_val = 1
    val = 1 # Fibonacci starts with 1
    inc = 0

    while (len(str(val)) < count):
        temp = last_val
        last_val = val
        val += temp
        inc += 1
    
    return inc + 2

if __name__ == '__main__':
    print "Answer : %d" % (fibo_dig_count(1000))
