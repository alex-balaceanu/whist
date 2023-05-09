class Card:
    def __init__(self, value: str, symbol: str):
        self.value = value
        self.symbol = symbol
        self.trump_value = 0
    cards_values = {'A': 15, 'K': 14, 'Q': 13, 'J': 12, '10': 10, '9': 9,
                    '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    def __gt__(self, other):
        if self.trump_value > other.trump_value:
            return True
        elif self.trump_value == other.trump_value:
            return self.cards_values[self.value] > self.cards_values[other.value]
        else:
            return False

    def __lt__(self, other):
        return self.cards_values[self.value] < self.cards_values[other.value]

    def __eq__(self, other):
        return self.cards_values[self.value] == self.cards_values[other.value]

    def __repr__(self):
        return f"{self.value} of {self.symbol}"

    def __str__(self):
        return f"{self.value} of {self.symbol}"


class Deck:
    def __init__(self):
        self.cards = []

    def initialize_deck(self):
        pass


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class Game:
    def __init__(self):
        pass

    def trump_card(self):
        pass

"""
TODO:
*trump card should be selected in Game class
*3 trump values 0 1 2, when hand size == 8 -> only 1 trump value - how to handle?
*select number of cards at the beginning of the game
*shuffle method
*populate deck method
*anti-cheat method
*display cards method
*display current trick
*keep track of won hands for every player and scores
*set steps order!!
"""
