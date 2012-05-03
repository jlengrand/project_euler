#!/usr/bin/env python 
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 33 of Project Euler
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
''' 
def simplify(num, den):
    """
    Tries to simplify the fraction in a dumb way, returns null otherwise
    TODO : Write in a nicer way
    """
    if str(num)[0] == str(den)[0]:
        return (int(str(num)[1]),int(str(den)[1]))
    elif str(num)[1] == str(den)[0]:
        return (int(str(num)[0]),int(str(den)[1]))     
    elif str(num)[0] == str(den)[1]:
        return (int(str(num)[1]),int(str(den)[0]))     
    elif str(num)[1] == str(den)[1]:
        return (int(str(num)[0]),int(str(den)[0]))     
    else:
        return None

def non_trivial_simpl():
    """
    Searches for all fractions that can be simplified in a curious way
    """
    # We want to have fractions less than one
    fin_nums = 1
    fin_dens = 1
    for den in range(11, 100):
        for num in range(10, den):
            if '0' not in str(den): # avoiding trivial examples
                res = simplify(num, den)
                if res != None:
                    if ((res[1] != 0) and(float(num)/den == float(res[0])/res[1]) ):
                        fin_nums *= res[0]
                        fin_dens *= res[1]
    
    return fin_dens / fin_nums # I do this because I know I can
    
if __name__ == '__main__':
    print "Answer : %d " % (last_ten())