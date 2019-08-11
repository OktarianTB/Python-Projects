import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.value + " of " + self.suit


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(s,v) for s in suits for v in values]

    def __repr__(self):
        number_of_cards = Deck.count(self)
        return "Deck of " + str(number_of_cards) + " cards"

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        number_of_cards = Deck.count(self)
        to_deal = min([number_of_cards, number])
        if number_of_cards == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-to_deal:]
        self.cards = self.cards[:-to_deal]
        return cards

    def shuffle(self):
        if Deck.count(self) == 52:
            random.shuffle(self.cards)
            return self.cards
        raise ValueError("Only full decks can be shuffled")

    def deal_card(self):
        return Deck._deal(self, 1)[0]

    def deal_hand(self, number):
        return Deck._deal(self, number)

