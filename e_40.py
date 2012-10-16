#!/usr/bin/env python
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : 16 - 10 - 2012
 #
 # DESCRIPTION : Solves problem 40 of Project Euler
 An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the following expression.
d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

This first version is going to be over dumb. We are actually going to create the fractional part.
We first need to know how much elements we need to sum.
 ##---
 """


def el_to_go(max_val=1000000):
    """
    Returns the maximum number of the range we are going to need to be able to get d_1000000
    """
    return 1000000  # max index is 100000. Dumbest limit is thus 1000000


def get_index(myfrac, el):
    """
    Given the string representation of the fractional part, return the elth element
    """
    return int(myfrac[el - 1])


def sum_elements():
    """
    Returns the value of the following expression.
    d_1  d_10  d_100  d_1000  d_10000  d_100000  d_1000000
    """
    els_to_go = [1, 10, 100, 1000, 10000, 100000, 1000000]
    max_el = el_to_go()
    sum_res = 1
    frac = ''.join(map(str, range(1, max_el + 1)))
    for el in els_to_go:
        sum_res *= get_index(frac, el)

    return sum_res

if __name__ == '__main__':
    print "Answer : %d " % (sum_elements())
