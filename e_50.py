#!/usr/bin/env python
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : 17 - 10 - 2012
 #
 # DESCRIPTION : Solves problem 50 of Project Euler
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds
to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand
that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of
the most consecutive primes?
 ##---
 """
import pickle

# list of primes up to one million.
plist = pickle.load(open("primes_list.dup", "rb"))


def is_prime(val):
    """
    Returns True if the number is prime
    """
    return (val in plist)


def sum_cons_primes(prime_list, max_val=1000000):
    """
    Returns the prime that can be written as the sum of
    the most consecutive primes below one-million.
    """
    max_cons = 0
    max_prime = 0
    for el in prime_list:
        if (prime_list.index(el)) % 10 == 0:
            print "%d/%d" % (prime_list.index(el), len(prime_list))
        cur_prime = el
        cur_ind = prime_list.index(el)
        nb_cons = 1
        while cur_ind < len(prime_list) - 1 and cur_prime < max_val:
            if is_prime(cur_prime):
                if nb_cons > max_cons :
                    max_cons = nb_cons
                    max_prime = cur_prime

            nb_cons += 1
            cur_ind += 1
            cur_prime += prime_list[cur_ind]

    return max_prime, max_cons

if __name__ == '__main__':
    print "Answer : %d " % (sum_cons_primes(plist)[0])
