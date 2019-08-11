import unittest
from deck_of_cards import Card, Deck


class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "6")

    def test_repr(self):
        self.assertEqual(self.card.__repr__(), "6 of Hearts")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_number_of_card(self):
        self.assertEqual(self.deck.count(), 52)

    def test_values(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for card in self.deck.cards:
            self.assertIn(card.suit, suits)
            self.assertIn(card.value, values)

    def test_shuffle(self):
        self.assertNotEqual(self.deck.cards[0], self.deck.shuffle()[0])

    def test_deal_cards(self):
        self.assertEqual(len(self.deck.deal_hand(5)), 5)
        self.assertNotIn(self.deck.deal_hand(5), self.deck.cards)


if __name__ == "__main__":
    unittest.main()