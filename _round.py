"""
One round of blackjack
"""

from ._deck import Deck
from ._playerhand import PlayerHand
from ._dealerhand import DealerHand

class Round():
    """ Object that defines one round of blackjack """
    def __init__(self, player_name='Human'):
        """
            Attributes:
            player_name (str)
            deck (Deck)
            player_hand (PlayerHand)
            dealer_hand (DealerHand)
            outcome (str): 'Loss', 'Draw', 'Win', 'In Progress'
        """
        self.player_name = player_name
        # opening message
        print('Starting new round of game!')
        # initialize deck
        self.deck = Deck()
        # initialize player and dealer hands
        self.player_hand = PlayerHand(owner=player_name)
        self.dealer_hand = DealerHand(owner='Dealer')
        # deal two cards each to both player and dealer
        self.player_hand.deal(self.deck)
        self.dealer_hand.deal(self.deck)
        # initialize outcome
        self.outcome = 'In Progress'