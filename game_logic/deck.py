import random
import logging


class Deck:
    def __init__(self, all_cards) -> None:
        super().__init__()
        self.remaining_cards = all_cards
        self.active_cards = []
        self.discarded_cards = []

    def shuffle(self):
        random.shuffle(self.remaining_cards)

    def pick(self):
        if len(self.remaining_cards) != 0:
            picked_card = self.remaining_cards.pop(0)
            self.active_cards.append(picked_card)
        else:
            logging.info("The main deck is empty, discarded deck has been reshuffled.")
            self.remaining_cards = self.discarded_cards.copy()
            self.discarded_cards = []
            self.shuffle()
            picked_card = self.pick()
        return picked_card

    def discard(self, card):
        try:
            self.active_cards.remove(card)
        except IndexError:
            print("This card is not from that deck")
        else:
            self.discarded_cards.append(card)
