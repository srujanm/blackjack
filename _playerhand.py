"""
PlayerHand object
"""

from ._hand import Hand

class PlayerHand(Hand):
    """
    PlayerHand object is derived from Hand
    Has methods to detect if hand is bust or blackjack
    """
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