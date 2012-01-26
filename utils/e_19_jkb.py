#! /usr/bin/env python

# 2009/03/30 - euler019.py
# Solution au Probleme 19 de Project Euler
# http://projecteuler.net/index.php?section=problems&id=19
# Jean Karim Bockstael - jkb@jkbockstael.be

# Not used to create the algorithm, but to debut it :s. 
#This solution is way more elegant though !

from datetime import *

def euler19(beginyear, endyear):
    count = 0
    for year in range(beginyear, endyear + 1):
        for month in range (1, 13):
            if date(year, month, 1).weekday() == 6:
                print date(year, month, 1)
                count += 1
    return count
    
print euler19(1901, 2000)
raw_input()