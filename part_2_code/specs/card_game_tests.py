import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.four_of_clubs = Card("clubs", 4)
        self.ace_of_spades = Card("spades", 1)
        self.queen_of_hearts = Card("hearts", 12)
        
        self.card_game = CardGame()

    def test_check_for_ace_is_ace(self):
        actual = self.card_game.check_for_ace(self.ace_of_spades)
        self.assertEqual(True, actual)

    def test_check_for_ace_not_ace(self):
        actual = self.card_game.check_for_ace(self.four_of_clubs)
        self.assertEqual(False, actual)

    def test_highest_card(self):
        actual = self.card_game.highest_card(self.four_of_clubs, self.queen_of_hearts)
        expected = self.queen_of_hearts
        self.assertEqual(expected, actual)

    def test_cards_total_one_card(self):
        actual = self.card_game.cards_total([self.queen_of_hearts])
        expected = "You have a total of 12"
        self.assertEqual(expected, actual)

    def test_cards_total_many_cards(self):
        actual = self.card_game.cards_total([self.queen_of_hearts, self.ace_of_spades, self.four_of_clubs])
        expected = "You have a total of 17"
        self.assertEqual(expected, actual)