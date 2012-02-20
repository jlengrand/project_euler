#!/usr/bin/env python 
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 32 of Project Euler
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
''' 

def all_permutations(seq):
    """permutates a sequence and return a list of the permutations"""
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]
            for m in all_permutations(part):
                temp.append(seq[k:k+1] + m)
        return temp

def combinations(iterable, r):
    """
    Return r length subsequences of elements from the input iterable
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    """
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def all_combinations(iterable, r):
    """
    Overlays combinations functions in order to get a list of integers including all permutations
    should be kept as a generator!
    """
    out_list = []
    
    combs = combinations(iterable, r)
    for comb in combs:
        numLists = all_permutations(comb)
        [out_list.append(to_nums(numList)) for numList in numLists]
        
    return out_list
        

def to_nums(list_num):
    """Returns an integer given a list of numbers"""
    return int(''.join(map(str,list_num)))
    

def is_pandigital(plier, plicand, product):
    """
    Well, it works this way ^^
    Returns True if the multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital
    """
    ref_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_list = [str(product), str(plier), str(plicand)]
    
    if ref_list == sorted([int(item) for sublist in my_list for item in sublist]):
        return True
    else:
        return False

def test_combinations():
    """
    Tests all possible combinations of multipliers and multiplicands
    """
    res_list = []
    
    len_a = 1
    up_ref_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len_a < 4 : #  4 + 4 = 1 impossible
        combs_a = all_combinations(up_ref_list, len_a) # lists all possibilities
        max_b = (9 - len_a) / 2
        for comb_a in combs_a:
            up_ref_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            remove_list_els(up_ref_list, comb_a)
            for len_b in range(len_a, max_b + 1):
                combs_b = all_combinations(up_ref_list, len_b) # lists all possibilities
                for comb_b in combs_b:
                    prod = comb_a * comb_b
                    if is_pandigital(comb_a, comb_b, prod):
                        res_list.append(prod)
                    
        up_ref_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]      
        len_a += 1
        
    return sum(remove_duplicates(res_list)) # removes duplicates
    
def remove_list_els(my_list, my_int):
    """Remove all elements of my_int from my_list"""
    [my_list.remove(int(val))  for val in str(my_int)]
    # no need to return anything

def remove_duplicates(my_list):
    """Removes duplicates in a list"""
    return list(set(my_list))

if __name__ == '__main__':
    print "Answer : %d " % (test_combinations())
