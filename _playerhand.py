"""
PlayerHand object
"""
from ._hand import Hand

class PlayerHand(Hand):
    """
    PlayerHand object is sub-classed from Hand
    """
    def __str__(self):
        """
        Returns string listing cards in hand
        """
        card_str = 'Your cards:\n'
        for card in self.display():
            card_str += card + '\t'
        return card_str

    def is_bust(self):
        """
        Checks if hand is bust

        Returns:
            (bool)
        """
        return min(self.score(ace_value=1), self.score(ace_value=11)) > 21

    def is_blackjack(self):
        """
        Checks if hand is blackjack

        Returns:
            (bool)
        """
        return self.score(ace_value=1) == 21 or self.score(ace_value=11) == 21