"""
Script with blackjack game implementations
"""

from ._deck import Deck, CARD_NAMES, CARD_VALUES, CARD_DICT
from ._playerhand import PlayerHand
from ._dealerhand import DealerHand

def blackjack(player_name='HUMAN'):
    """
    Main function

    Inputs:
        player_name (str): name of player

    Returns:
        (int): -1 for loss, 0 for draw, 1 for win
    """

    # opening message
    print('Starting new round of game!')
    # initialize deck
    blackjack_deck = Deck()
    # initialize player and dealer hands
    player_hand = PlayerHand(owner=player_name)
    dealer_hand = DealerHand(owner='Dealer')
    # deal two cards each to both player and dealer
    player_hand.deal(blackjack_deck)
    dealer_hand.deal(blackjack_deck)

    # start the round
    # round outcome indicator to be returned by function
    round_outcome = None
    while True:
        # print player hand and one card from dealer hand
        print(player_hand)
        dealer_hand.show_one()
        # check for blackjack
        if player_hand.is_blackjack():
            round_outcome = 1
            print('You have a blackjack! :D')
            break
        # check for bust
        elif player_hand.is_bust():
            round_outcome = -1
            print('Your hand is bust :(')
            break
        # if neither, then request move from player
        # if player requests to hit, draw a card
        elif request_move() is 'h':
            # draw a card from the deck
            player_hand.hit(blackjack_deck)
        # if player requests to stand, initiate dealer sequence
        elif request_move() is 's':
            print('Starting dealer moves')
            pass
        # if player enters a wrong input, do nothing
        else:
            pass
    else:
        print('End of round!')

def request_move():
    """
    Sub-function of blackjack() which requests player input for a move

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