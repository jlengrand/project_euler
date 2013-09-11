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

card_order = [1, 2, 3]

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

class Poker:
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

class PokerGame:
    """
    A game is defined as two players having a hand of 5 cards each.
    """
    def __init__(self, hand_1, hand_2):
        self.hand_1 = hand_1
        self.hand_2 = hand_2

class Hand:
    def __init__(self, cards):
        self.cards = cards # should be 5

class Card:
    _values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    _colors = ["H", "C", "S", "D"]
    def __init__(self, value, color):
        self.value = value
        self.color = color

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
        return Hand(poker_cards)

    games = [PokerGame(create_hand(game[0]), create_hand(game[1]))  for game in data]
    return games


def sort_hands(hands):
    #FIXME: Not working. To refactor
    def sort_hand(hand):
        """
        Sorts a hand of cards in descending order.
        There should be no reference to card color
        """
        sorted_hand = list(hand)
        sorted_hand.sort(key=lambda x: card_order.index(x[0]), reverse=True)
        return sorted_hand
    sorted_hands = [[sort_hand(h) for h in hand] for hand in hands]
    #need to sort now
    return sorted_hands

def winning_hands(filename, player=1):
    """
    Returns the number of winning hands for player 1 or 2
    """
    data = load_data(filename)
    games = create_games(data)

    #data = sort_hands(hands)
    #print hands

        # player_hand = data[0][0]
        # player_card = player_hand[0]

        # card = Card(player_card[0], player_card[1])
        # print card.value
        # print card.color

        # print player_hand

        # print Hand.Values.reverse_mapping['K']
    # we want to knwo what is his rank
    #get_rank(player_hand)

if __name__ == '__main__':
    winning_hands("./e_54_poker.txt")
    #print 1
    #print "Answer : %d " % (winning_hands("./e_54_poker.txt"))