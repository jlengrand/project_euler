#!/usr/bin/env python
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : 16 - 10 - 2012
 #
 # DESCRIPTION : Solves problem 56 of Project Euler
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b  100,
what is the maximum digital sum?
 ##---
 """


def sum_numbers(val):
    """
    Given an value, returns the sum of all its numbers
    """
    temp = str(val)
    res = sum([int(i) for i in temp])
    return res


def sum_pow(max_a, max_b=None):
    """
    given val_a and val_b, returns the maximum sum of all numbers of form a^b,
    where a < max_a and b < max_b
    If val_b is None, max_a = max_b
    """
    if max_b is None:
        max_b = max_a

    max_val = 0
    for cur_a in xrange(1, max_a + 1):
        for cur_b in xrange(1, max_b + 1):
            cur_val = sum_numbers(pow(cur_a, cur_b))
            if cur_val > max_val:
                max_val = cur_val
    return max_val


if __name__ == '__main__':
    print "Answer : %d " % (sum_pow(100))
