"""
DealerHand object
"""

from ._hand import Hand

class DealerHand(Hand):
    """
    DealerHand object is sub-classed from Hand
    """
    def __str__(self):
        """
        Returns string listing cards in hand
        """
        card_str = 'Dealer cards:\n'
        for card in self.display():
            card_str += card + '\t'
        return card_str

    def show_one(self):
        """
        Prints out only first card in hand
        """
        print('Dealer card:')
        print(self.display()[0])

    def is_bust(self):
        """
        Checks if hand is bust

        Returns:
            (bool)
        """
        return min(self.score(ace_value=1), self.score(ace_value=11)) > 17

    def is_blackjack(self):
        """
        Checks if hand is blackjack

        Returns:
            (bool)
        """
        return self.score(ace_value=1) == 17 or self.score(ace_value=11) == 17