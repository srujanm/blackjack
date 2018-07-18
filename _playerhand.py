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
