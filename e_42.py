#!/usr/bin/env python 
'''
Created on 7 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 42 of Project Euler
The nth term of the sequence of triangle numbers is given by, t_n = 1/2 * n * (n+1); 
so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding 
to its alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using e_42.data (right click and 'Save Link/Target As...'), 
a 16K text file containing nearly two-thousand common English words, 
how many are triangle words?
''' 
import string

def load_data(filename):
    """
    Loads the data from a name file into a table
    """
    my_file = open(filename, "r")
    line = my_file.readline()
    data = [el for el in line.split("\"")][1::2]
    my_file.close()        
    return data

def dict_alphabet():
    """
    Returns a dict of the alphabet, with value for each letter.
    """
    alpb= dict()
    letters = string.ascii_uppercase
    inc = 1
    for j in range(len(letters)): 
        alpb[letters[j]] = inc
        inc += 1

    return alpb

def names2scores(data):
    """
    Returns a list of scores given a list of names.
    Scores are calculated with word values, (A = 1, B = 2, ...)
    """
    scores = []
    alpb = dict_alphabet()
    for name in data:
        score = 0
        for jj in range(len(name)):
            score += (alpb[name[jj]])
    
        scores.append(score)
    
    return scores

def triangle_list(max_val):
    """
    Returns a list of triangle numbers up to max_val.
    triangle_numbers is an increasing function.
    """
    trilist = []
    ptr = 1
    val = 1
    while val < max_val:
        val = trinum(ptr)
        trilist.append(val)
        ptr += 1 
    
    return trilist

def trinum(val):
    """
    Returns the triangle number for a given value
    """
    return val * (val + 1) / 2

def triangle_words(filename):
    """
    Returns the number of triangle words in filename
    """
    data = load_data(filename)
    scores = names2scores(data)
    trilist = triangle_list(max(scores))
    
    # checking if words are triangle
    cpt = 0
    for score in scores:
        if score in trilist:
            cpt += 1
            
    return cpt
    
if __name__ == '__main__':    
    print "Answer : %d " % (triangle_words("e_42.data"))