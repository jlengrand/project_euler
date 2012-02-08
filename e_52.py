'''
Created on 7 feb. 2012

@author: Julien Lengrand-Lambert
DESCRIPTION : Solves problem 52 of Project Euler
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
def smallest_match(max_mul):
    """
    Find the smallest positive integer, x, such that ..., till max_mul*x contain the same digits.
    """
    cpt = 2
    nlist = [(i + 1) * cpt for i in range(max_mul)]
    
    while(1):
        if cpt % 10000 == 0:
            print cpt
        if same_size(nlist):
            if same_digits(nlist):
                print cpt, nlist
                return cpt

        cpt += 1
        nlist = [(i + 1) * cpt for i in range(max_mul)]

def all_permutations(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]
            for m in all_permutations(part):
                temp.append(seq[k:k+1] + m)
        return temp


def same_digits(nlist):
    """
    Returns True if all numbers in nlist contain the same digits. 
    Which means they are all permutations of the first value 
    """
    perms = all_permutations(str(nlist[0])) # finds all permutations
    for el in nlist:
        if not(str(el) in perms):
            return False      
    
    return True

def same_size(nlist):
    """
    Returns True if all numbers in nlist have the same number of digits
    """
    nlen = len(str(nlist[0]))
    for el in nlist :
        if len(str(el)) != nlen:
            return False
    return True

if __name__ == '__main__':
    print "Answer : %d " % (smallest_match(6))  