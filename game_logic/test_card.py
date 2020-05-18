from unittest import TestCase
from game_logic.card import BlackCard


class TestBlackCard(TestCase):
    def test_split_into_chunks_0_blank(self):
        card = BlackCard('test', "Why can't I sleep at night?", 1)
        expected_chunks = ["Why can't I sleep at night?"]
        actual_chunks = card.split_into_chunks()
        self.assertListEqual(expected_chunks, actual_chunks)

    def test_split_into_chunks_1_blank(self):
        card = BlackCard('test', "I got 99 problems but _ ain't one.", 1)
        expected_chunks = ["I got 99 problems but", "ain't one."]
        actual_chunks = card.split_into_chunks()
        self.assertListEqual(expected_chunks, actual_chunks)

    def test_split_into_chunks_2_blanks(self):
        card = BlackCard('test', 'And the Academy Award for _ goes to _.', 2)
        expected_chunks = ["And the Academy Award for", "goes to", "."]
        actual_chunks = card.split_into_chunks()
        self.assertListEqual(expected_chunks, actual_chunks)
