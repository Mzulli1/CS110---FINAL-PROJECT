"""
Mark A. Zulli
Final Project Idea 1
November 2017
"""

import requests

SUITS = {0: 'spades',
         1: 'hearts',
         2: 'clubs',
         3: 'diamonds',
         }

VALUES = {"0": ["ace", [11, 1]],
          "1": ["two", [2]],
          "2": ["three", [3]],
          "3": ["four", [4]],
          "4": ["five", [5]],
          "5": ["six", [6]],
          "6": ["seven", [7]],
          "7": ["eight", [8]],
          "8": ["nine", [9]],
          "9": ["ten", [10]],
          "10": ["jack", [10]],
          "11": ["queen", [10]],
          "12": ["king", [10]]
          }

CARDS_PER_SUIT = 13
CARDS_PER_DECK = len(SUITS) * CARDS_PER_SUIT
URL = 'https://api.random.org/json-rpc/1/invoke'
API_KEY = 'a5040d0a-2388-4d90-a800-01255bdb3e7a'


class Deck:
    __all_cards = []

    #class constructor
    def __init__(self, num_decks=1):
        # LIST OF CARD OBJECTS
        self.__num_decks = num_decks
        self.__cards = []
        # MAKES A DEFAULT UNSHUFFLED DECK
        for i in range(0, CARDS_PER_DECK*num_decks):
            self.__all_cards.append(Card(i))
            self.__cards.append(Card(i))

    def validate_deck(self):
        return len(self.__cards) >= 1

    def shuffle(self):
        payload = {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": API_KEY,
                "n": len(self.__cards)-1,
                "min": 0,
                "max": len(self.__cards)-1,
                "replacement": False
            },
            "id": 1111
        }
        r = requests.post(URL, json=payload)
        data = r.json()
        order = data['result']['random']['data']
        shuffled_deck = []
        for position in order:
            shuffled_deck.append(self.__cards[position])
        self.__cards = shuffled_deck

    def full_shuffle(self):
        self.__cards = self.__all_cards
        self.shuffle()

    def deal_card(self):
        return None if len(self.__cards) == 0 else self.__cards.pop(0)

    def all_cards(self):
        return self.__all_cards


class Card:

    def __init__(self, number, joker=False):
        if joker == True:
            self.__suit
        else:
            self.__suit = SUITS[(number // CARDS_PER_SUIT) % len(SUITS)]
            self.__name = VALUES[str(number % CARDS_PER_SUIT)][0]
            self.__value = VALUES[str(number % CARDS_PER_SUIT)][1]


    def __str__(self):
        return '%s of %s' % (self.__name, self.__suit)

    def name(self):
        return self.__name

    def value(self):
        return self.__value

    def suit(self):
        return self.__suit


def main():
    d = Deck(1)
    list_of_cards = []
    for i in range(52):
        list_of_cards.append(d.deal_card())

    for card in list_of_cards:
        print(str(card), card.value(), card.suit(), card.name())
    print(len(list_of_cards))
    print(str(d.deal_card()))
    print(list_of_cards.count('ace of spades'))

main()



