#!/usr/bin/env python
'''
Created on 11 sept. 2013

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 54 of Project Euler
The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated
    cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

How many hands does Player 1 win?
'''

def load_data(filename):
    """
    Loads the given file according to the problem description.
    Returns a list of two hands of poker players.
    """
    cards_in_poker = 5
    hands = []
    file = open(filename, "r")

    #for line in file :
    for i in range(2):
        res = file.readline().rstrip() # also removes eol
        res_spl = res.split(" ")

        # creating left and right player's hands
        left = res_spl[:cards_in_poker]
        right = res_spl[cards_in_poker:]

        hands.append([left, right])

    file.close()
    return hands

def sort_n_strip(hands):
    """
    As description indicates data is correct, we can ignore the color of the
    cards. (and hence strip the value)
    We also want to sort the players hands (to be worked with easier later)
    """
    # just keeping the first element of the cards
    stripped_hands =  [[[val[0] for val in h] for h in hand] for hand in hands]

    sorted_hands = stripped_hands
    #need to sort now
    return sorted_hands

def winning_hands(filename):
    """
    Returns the first of the firs num consecutive primes.
    """
    hands = load_data(filename)

    data = sort_n_strip(hands)
    print hands
    print data

    #for val in hands:

        #print val

if __name__ == '__main__':
    winning_hands("./e_54_poker.txt")
    #print 1
    #print "Answer : %d " % (winning_hands("./e_54_poker.txt"))