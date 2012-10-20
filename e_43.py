#!/usr/bin/env python
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 43 of Project Euler
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

Will be very long due to dumb implementation.
Would be way better with a generator implementation of all_permutations already
'''
my_primes = [2, 3, 5, 7, 11, 13, 17]


def all_permutations(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k + 1:]
            for m in all_permutations(part):
                temp.append(seq[k:k + 1] + m)
        return temp


def is_cool(str_number):
    """
    Returns True of number (in a string form) has the cool divisible property
    """
    for i in range(len(str_number) - 3):
        cur = str_number[i + 1:i + 4]
        if (int(cur) % my_primes[i]) != 0:
            return False
    return True


def find_cool_pandigital():
    """
    Returns the sum of all 0 to 9 pandigital numbers with cool property.
    """
    cases = all_permutations("1234567890")
    cool = []
    cpt = 0
    for case in cases:
        #if int(case[0]) != 0:
            # check for cool property
        if is_cool(case):
            cool.append(int(case))

    print cool
    print len(cool)
    return sum(cool)

if __name__ == '__main__':
    print "Answer : %d " % (find_cool_pandigital())
