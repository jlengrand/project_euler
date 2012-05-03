#!/usr/bin/env python 
'''
Created on 2 may 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 38 of Project Euler
Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n >1?
''' 
def has_duplicates(mylist):
    """
    Returns True if the list contains at least one duplicate
    """
    return (len(mylist)!=len(set(mylist)))

def concat_pandigital():
    """
    Returns the largest 1 to 9 pandigital number formed as the concatened product of an integer with (1, 2, ..., n)
    """
    pand_list = []
    # max_val is number for which sum(len(max_val * 1) + len(max_val * 2) ) > 9  = 10000
    for x in range(1, 10000):
        got = "" # list of all numbers we already have
        mul = 1
        doit = 1
        while doit:
            cur_val = x * mul
            if (("0" in str(cur_val)) or (has_duplicates(got + str(cur_val)))):
                doit = 0
            else:
                got += str(cur_val)
                mul += 1
        
        if len(got) == 9: # we have a pandigital number in output
            print x
            pand_list.append(int(got)) # should put got back in a correct way

    return max(pand_list)

if __name__ == '__main__':
    print "Answer : %d " % (concat_pandigital())