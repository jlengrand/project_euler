#!/usr/bin/env python 
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : Mon Jan 16 17:11:30 CET 2012
 #
 # DESCRIPTION : Solves problem 22 of Project Euler
 Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this 
 value by its alphabetical position in the list to obtain a name score.
 For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.
 What is the total of all the name scores in the file?
 ##---
"""
def names_scores(filename):
    """
    Returns the total of all the name scores in filename
    """
    data = load_data(filename)
    
    
    return 1

def load_data(filename):
    """
    Loads the data from a name file into a table
    """
    file = open(filename, "r")
    line = file.readline()
    data = [el for el in line.split("\"")][1::2]
    file.close()        
    return data

if __name__ == '__main__':
    data = load_data("e_22.data")
    #print "Answer : %d" % (names_scores("e_22.data"))
