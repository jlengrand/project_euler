#!/usr/bin/env python
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : Thu Jan 19 10:12:06 CET 2012
 #
 # DESCRIPTION : Solves problem 26 of Project Euler
 A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

 1/2	= 	0.5
 1/3	= 	0.(3)
 1/4	= 	0.25
 1/5	= 	0.2
 1/6	= 	0.1(6)
 1/7	= 	0.(142857)
 1/8	= 	0.125
 1/9	= 	0.(1)
 1/10	= 	0.1
 Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

 Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
 ##---
 """
import decimal as d
import re

def repetitions(s):
   r = re.compile(r"(.+?)\1+")
   for match in r.finditer(s):
       yield (match.group(1), len(match.group(0))/len(match.group(1)))

def getDecimal(nume, deno):
    """
    Returns decimals of nume / deno as a string
    """
    return str(d.Decimal(nume) / d.Decimal(deno))[2:] # to remoe the 0. part

def longest_recurring(max_val):
    """
    Returns the number between 1/2 and 1/max val having the longest recurring cycle
    in its decimal fraction part
    """
    fin_val = 0
    longest = 0
    for val in range(2, max_val + 1):
        myFrac = getDecimal(1, val)
        myReps = list(repetitions(myFrac))
        try:
            temp = max(myReps, key=lambda x: len(x[0]))
            big = len(temp[0])
            if big > longest:
                longest = big
                fin_val = val
        except ValueError:
            pass

    return fin_val, longest

if __name__ == '__main__' :
    d.getcontext().prec = 2000
    res = longest_recurring(1000)
    print "Number with longest recurring cycle is : %d" % (res[0])