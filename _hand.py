"""
Hand object
"""

from ._deck import CARD_NAMES, CARD_VALUES, CARD_DICT

class Hand():

    """Implements a hand of cards"""

    def __init__(self, card_names=CARD_NAMES, card_count=13*[0], owner=None):
        """
        Attributes:
            cards (dict {str, int}): dict with card names as keys and corresponding card counts as values
            owner (str): Name of owner of hand

        """
        self.cards = dict(zip(card_names, card_count))
        self.owner = owner

    def hit(self, blackjack_deck):
        """
        Draws a random card from input deck and adds it to hand

        Inputs:
            blackjack_deck (Deck): deck from which card needs to be drawn
        """
        self.cards[blackjack_deck.draw()] += 1

    def deal(self, blackjack_deck):
        """
        Implements initial deal of two cards

        Inputs:
            blackjack_deck (Deck): deck from which card needs to be drawn
        """
        self.hit(blackjack_deck)
        self.hit(blackjack_deck)

    def display(self):
        """
        Displays all cards in hand. Same as Deck.display()

        Returns:
            list(str): list of all card names in hand (with repetition)
        """
        raw_hand = []
        for card_char, card_count in self.cards.items():
            if card_count > 0:
                raw_hand.extend(card_count*[card_char])

        return raw_hand

    def is_soft(self):
        """
        Checks if hand is soft, i.e. if it contains an ace

        Returns:
            (bool)
        """
        return self.cards['A'] > 0

    def score(self):
        """
        Calculates score of hand
        Returns:
            (int)
        """
        score_without_aces = sum([CARD_DICT[card] for card in self.display() if card != 'A'])
        # if hand is hard, simply return score_without_aces
        if not self.is_soft():
            return score_without_aces

        # if hand is soft, choose between higher and lower bounds for score
        else:
            # with one ace
            if self.cards['A'] == 1:
                score_higher = score_without_aces + 11
                score_lower = score_without_aces + 1
                if score_higher <= 21:
                    return score_higher
                else:
                    return score_lower
            # with multiple aces
            else: 
                score_higher = score_without_aces + 11 + (self.cards['A']-1)
                score_lower = score_without_aces + 1 + (self.cards['A']-1)
                if score_higher <= 21:
                    return score_higher
                else:
                    return score_lower

    def is_bust(self):
        """
        Checks if hand is bust

        Returns:
            (bool)
        """
        return self.score > 21

    def is_blackjack(self):
        """
        Checks if hand is blackjack

        Returns:
            (bool)
        """
        return self.score == 21
