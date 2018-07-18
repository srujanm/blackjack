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
            player_status (str): 'Normal', 'Bust', 'Blackjack'
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
        # initialize player status and outcome
        self.player_status = 'Normal'
        self.outcome = 'In Progress'

    def set_outcome(self, new_outcome):
        """Method to change outcome of round"""
        if new_outcome not in ['Loss', 'Draw', 'Win', 'In Progress']:
            raise Exception('Invalid value of player_outcome')
        else:
            self.outcome = new_outcome

    def player_sequence(self):
        """Method to implement all player moves in round"""
        def request_move():
            """
            Sub-function of player_sequence() which accepts player input for a move
            Returns:
                (str)
            """
            print('Choose your move: Enter h to hit and s to stand')
            move = input()
            # check for validity of input
            if move != 'h' and move != 's':
                print('Invalid input! Try again')
                return None
            else:
                return move    
        # begin player loop
        while True:
            # print player hand and one card from dealer hand
            print(self.player_hand)
            self.dealer_hand.show_one()
            # check for blackjack
            if self.player_hand.is_blackjack():
                self.player_status = 'Blackjack'
                print('You have a blackjack! :D')
                break
            # check for bust
            elif self.player_hand.is_bust():
                self.outcome = 'Loss'
                self.player_status = 'Bust'
                print('Your hand is bust :(')
                break
            # if neither, then request move from player
            else:
                move = request_move()
                # if player requests to hit, draw a card
                if move is 'h':
                    self.player_hand.hit(self.deck)
                # if player requests to stand, break out of player loop
                elif move is 's':
                    break
                # if player enters wrong input, do nothing
                else:
                    pass

    def check_dealer_natural(self):
        """
        Method to check if dealer has a natural blackjack.
        Executed when the player gets a blackjack.
        """
        if blackjack_round.dealer_hand.is_natural_blackjack():
            self.outcome = 'Draw'
            print('And so does the dealer!')
            print(blackjack_round.dealer_hand)
        else:
            self.outcome = 'Win'
            print('And the dealer does not!')
            print(blackjack_round.dealer_hand)

    def dealer_sequence(self):
        """Method to implement dealer moves in a round"""
        # opening message
        print('Dealer will start drawing!')
        # start dealer loop
        while True:
            # print both player hand and dealer hand
            print(self.player_hand)
            print(self.dealer_hand)
