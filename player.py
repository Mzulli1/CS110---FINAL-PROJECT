"""
Mark A. Zulli
Final Project Idea 1
November 2017
"""

from deck import Deck

MAX_HAND = 21

class Player:
    # to be used by CPU when counting cards
    __observed = []

    def __init__(self):
        # list of cards in hand
        self.__hand = []

    def get_hand(self):
        return self.__hand

    def validate_player(self):
        hand_value = 0
        for card in self.__hand:
            hand_value += card.value()
        return hand_value > MAX_HAND

    def take(self, deck):
        card = deck.deal_card()
        self.__observed(card)
        self.__hand.append(card)

    def analyze(self, deck):
        cards_left = Deck.all_cards(deck) - self.__observed
        values_left = []
        for card in cards_left:
            values_left.append(card.get_value())

    def reset(self):
        self.__hand = []

