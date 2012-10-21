#!/usr/bin/env python
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : 17 - 10 - 2012
 #
 # DESCRIPTION : Solves problem 55 of Project Euler
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196,
never produce a palindrome.
A number that never forms a palindrome through the reverse
and add process is called a Lychrel number.
Due to the theoretical nature of these numbers,
and for the purpose of this problem, we shall assume that a number is Lychrel
until proven otherwise.
In addition you are given that for every number below ten-thousand,
it will either (i) become a palindrome in less than fifty iterations,
or, (ii) no one, with all the computing power that exists,
has managed so far to map it to a palindrome.

In fact, 10677 is the first number to be shown to require over fifty iterations
before producing a palindrome: 4668731596684224866951378664
(53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel
numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise
the theoretical nature of Lychrel numbers.
 ##---
 """

def is_palindromic(num):
    """
    Returns True if num is palindromic
    Ex : 121
    """
    return (num == reverse(num))

def reverse(num):
    """
    Returns the reverse number of num
    ex : 123 returns 321
    """
    str_num = str(num)
    rev = ''
    for i in range(len(str_num)):
        rev += str_num[len(str_num) - i - 1]

    return int(rev)


def is_lychrel(num, max_it=50):
    """
    Given a maximu number of iterations,
    returns True if num is a lychrel number
    """
    cur = num
    it = 1
    while it < max_it:
        cur = cur + reverse(cur)
        if is_palindromic(cur):
            return False
        it += 1

    return True


def count_lychrel(max_num, max_it=50):
    """
    Returns the number of lychrel numbers smaller than max_num
    The maximum iteration number defines how many times the process is repeated
    before considreing a number to be a lychrel number
    """
    lychrels = []
    for i in xrange(1, max_num + 1):
        if (is_lychrel(i, max_it)):
            lychrels.append(i)

    print lychrels
    return len(lychrels)


if __name__ == '__main__':
    print "Answer : %d " % (count_lychrel(10000))
