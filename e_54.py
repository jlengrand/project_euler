#!/usr/bin/env python
'''
Created on 11 sept. 2013

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 54 of Project Euler

Ranking Description
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated
    cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

How many hands does Player 1 win?
'''

from itertools import groupby

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

class PokerRanking:

    _ranks=enum("High_Card",
                "One_Pair",
                "Two_Pairs",
                "Three_of_a_Kind",
                "Straight",
                "Flush",
                "Full_House",
                "Four_of_a_Kind",
                "Straight",
                "Flush",
                "Royal_Flush")

    def calculate_hand_rank(self, hand):
        """
        Given a PokerHand, calculate its value
        The Poker hand is assumed to be sorted by value
        """

    def same_suit(self, hand):
        """
        Define whether all cards in the given hand have the same suit.
        Returns a boolean
        """
        first_color = hand.cards[0].color
        bools = [card.color == first_color for card in hand.cards]
        return (len([x for x in bools if x is True]) == len(bools))

class PokerGame:
    """
    A game is defined as two players having a hand of 5 cards each.
    """
    def __init__(self, hand_1, hand_2):  # Could be more. Use lists instead
        # Should be PokerHands
        self.hand_1 = hand_1
        self.hand_1_rank = 0
        self.hand_2 = hand_2
        self.hand_2_rank = 0

class PokerHand:
    def __init__(self, cards):
        # should be 5 cards in a poker hand.
        if len(cards) !=5 :
            raise AttributeError("A Poker hand should be 5 cards")
        # cards sorted on creation
        self.cards = cards
        self.sort_hand()

    def __str__(self):
        "How to print a full poker hand"
        hand = ""
        for card in self.cards:
            hand += card.__str__() + " "
        return hand

    def sort_hand(self):
        """
        Sorts a hand of cards in descending order.
        """
        sorted_hand = list(self.cards)
        sorted_hand.sort(key=lambda x: Card._values.index(x.value), reverse=True)
        self.cards = sorted_hand

class Card:
    _values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    _colors = ["H", "C", "S", "D"]
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        """
        How to print a card
        """
        return self.value + self.color

##

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

def create_games(data):
    """
    Transforms a list of lists of poker cards into proper Poker games
    """
    def create_hand(cards):
        """
        Create a poker hand out of a list of cards
        """
        if len(cards) != 5:
            raise AttributeError("Expecting 5 cards!")

        poker_cards = [Card(card[0], card[1]) for card in cards]
        return PokerHand(poker_cards)

    games = [PokerGame(create_hand(game[0]), create_hand(game[1]))  for game in data]
    return games

def winning_hands(filename, player=1):
    """
    Returns the number of winning hands for player 1 or 2
    """
    data = load_data(filename)
    games = create_games(data)

    my_game = games[0]
    my_hand = my_game.hand_1

    pok = PokerRanking()
    print pok.same_suit(my_hand)

    print [k for k, g in groupby('AAAABBBCCDAABBB')] #--> A B C D A B
    print [len(list(g)) for k, g in groupby('AAAABBBCCD')] #--> AAAA BBB CC D

    my_hand.cards[1].value = "K"
    print [k for k, g in groupby(my_hand.cards, lambda x : x.value)] #--> A B C D A B

if __name__ == '__main__':
    winning_hands("./e_54_poker.txt")
    #print 1
    #print "Answer : %d " % (winning_hands("./e_54_poker.txt"))