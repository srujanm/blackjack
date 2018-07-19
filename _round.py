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
        print('New round!\n')
        # initialize deck
        self.deck = Deck()
        # initialize player and dealer hands
        self.player_hand = PlayerHand(owner=player_name)
        self.dealer_hand = DealerHand(owner='Dealer')
        # deal two cards each to both player and dealer
        self.player_hand.deal(self.deck)
        self.dealer_hand.deal(self.deck)
        # initialize player status and round outcome
        self.player_status = 'Normal'
        self.outcome = 'In Progress'

    def player_sequence(self):
        """Method to implement all player moves in round"""
        def request_move():
            """
            Sub-function of player_sequence() which accepts player input for a move
            Returns:
                (str)
            """
            print('\nChoose your move: Enter h to hit and s to stand')
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
                print('\nYou have a blackjack! :D')
                break
            # check for bust
            elif self.player_hand.is_bust():
                self.outcome = 'Loss'
                self.player_status = 'Bust'
                print('\nYour hand is bust :(')
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
        if self.dealer_hand.is_blackjack():
            self.outcome = 'Draw'
            print('And so does the dealer!')
            print(self.dealer_hand)
        else:
            self.outcome = 'Win'
            print('And the dealer does not!')
            print(self.dealer_hand)

    def dealer_sequence(self):
        """Method to implement dealer moves in a round"""
        # opening message
        print('\nDealer will start drawing now!')
        # start dealer loop
        while True:
            # print both player hand and dealer hand
            print(self.player_hand)
            print(self.dealer_hand)
            # check for blackjack
            if self.dealer_hand.is_blackjack():
                self.outcome = 'Loss'
                print('\nDealer has a blackjack!')
                break
            # check for bust
            elif self.dealer_hand.is_bust():
                self.outcome = 'Win'
                print('\nDealer hand is bust!')
                break
            # check if dealer should draw
            elif self.dealer_hand.should_draw():
                print('\nDealer draws')
                self.dealer_hand.hit(self.deck)
            # else complete dealer hand
            else:
                print('\nDealer hand complete')
                break

    def compare_scores(self):
        """Method to compare scores of dealer and player hands"""
        score_diff = self.player_hand.score() - self.dealer_hand.score()
        if score_diff > 0:
            self.outcome = 'Win'
            print(f'You beat the dealer by {score_diff} points')
        elif score_diff == 0:
            self.outcome = 'Draw'
            print('You and the dealer have the same score!')
        else:
            self.outcome = 'Loss'
            print(f'The dealer beat you by {-score_diff} points')
