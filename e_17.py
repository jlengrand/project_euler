#!/usr/bin/env python 
"""
 ##---
 # Julien Lengrand-Lambert
 #Created on : Tue Jan 17 10:57:41 CET 2012
 #
 # DESCRIPTION : Solves problem 17 of Project Euler
 If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
 then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
 words, how many letters would be used?

 NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
 forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
 letters. The use of "and" when writing out numbers is in compliance with 
 British usage.
 ##---
"""
def letters_to_1000():
    """
    Returns the number of letters used from 1 to 1000
    """
        
    number_of_hundreds = 9
    number_of_ties = 8 * number_of_hundreds # tens are specials
    number_of_tens = 9
    number_of_thousands = 1
    number_of_unities = 10
    
    ands = ["and"]
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"] 
    ties = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ] 
    hundreds = ["hundred"] 
    thousands = ["thousand"]
    
    andl = char_list(ands) * number_of_hundreds * (100 - 1)
    numbersl = char_list(numbers) * (number_of_hundreds + 1) * number_of_tens
    hunpref = 100 * char_list(numbers) # one hundred, two hundred and so on. . . 
    tensl = char_list(tens) * (number_of_hundreds + 1)
    tiesl = char_list(ties) * (number_of_hundreds + 1) * number_of_unities
    hundredsl = char_list(hundreds) * number_of_hundreds * 100
    thousandsl = char_list(thousands) * number_of_thousands
    onethousand = 3 # for the "one" thousand
    
    return andl + numbersl + tensl + tiesl + hundredsl + thousandsl + hunpref + onethousand

def char_list(list_val):
    """
    Returns the total number of characters in a list
    """
    return sum([len(val) for val in list_val])

if __name__ == '__main__':
    print "Answer : %d" % (letters_to_1000())
