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
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


if __name__ == '__main__':
    aa = combinations_with_replacement(range(8), 8)
    val = 0
    for a in aa:
        print sum(a)
    print val