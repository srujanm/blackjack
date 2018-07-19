"""
DealerHand object
"""

from ._hand import Hand

class DealerHand(Hand):
    """
    DealerHand object is sub-classed from Hand
    """
    def __str__(self):
        """Returns string listing cards in hand"""
        card_str = 'Dealer cards:\n'
        for card in self.display():
            card_str += card + '\t'
        return card_str

    def show_one(self):
        """Prints out only first card in hand"""
        print('Dealer card:')
        print(self.display()[0])

    def should_draw(self):
        """
        Checks if dealer should draw based on score
        If the soft score is less than or equal to 17 or hard score is less than 17, dealer should draw
        """
        if self.is_soft():
            return self.score() <= 17
        else:
            return self.score() < 17