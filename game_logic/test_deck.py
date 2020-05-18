from unittest import TestCase
from game_logic.deck import Deck


class TestDeck(TestCase):
    def test_shuffle(self):
        deck = Deck([1, 2, 3])
        expected_length = 3
        deck.shuffle()
        actual_length = len(deck.remaining_cards)
        self.assertEqual(expected_length, actual_length)

    def test_pick_not_empty(self):
        deck = Deck([1, 2, 3])
        expected_picked_card = 1
        expected_active_cards = [1]
        actual_picked_card = deck.pick()
        actual_active_cards = deck.active_cards
        self.assertEqual(expected_picked_card, actual_picked_card)
        self.assertListEqual(expected_active_cards, actual_active_cards)

    def test_pick_empty(self):
        deck = Deck([1, 2, 3])
        deck.remaining_cards = []
        deck.active_cards = [1]
        deck.discarded_cards = [2, 3]
        deck.pick()

        expected_discarded_cards = []
        actual_discarded_cards = deck.discarded_cards
        self.assertEqual(expected_discarded_cards, actual_discarded_cards)
        self.assertEqual(2, len(deck.active_cards))

    def test_discard_is_in_active(self):
        deck = Deck([1, 2, 3])
        deck.active_cards = [1, 2]
        deck.remaining_cards = [3]

        deck.discard(2)

        expected_active_cards = [1]
        actual_active_cards = deck.active_cards
        expected_discarded_cards = [2]
        actual_discarded_cards = deck.discarded_cards
        self.assertListEqual(expected_active_cards, actual_active_cards)
        self.assertListEqual(expected_discarded_cards, actual_discarded_cards)
