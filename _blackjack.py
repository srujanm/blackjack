"""
Script with implementation of one blackjack round
"""

from ._round import Round

def blackjack_round(player_name='Human'):
    """
    Main function

    Inputs:
        player_name (str): name of player

    Returns:
        (int): -1 for loss, 0 for draw, 1 for win
    """
    # start a new round
    blackjack_round = Round(player_name)
    # initiate player sequence
    blackjack_round.player_sequence()
    """after player sequence"""
    # if player hand is bust, just go ahead and terminate round
    if blackjack_round.player_status is 'Bust':
        pass
    # if player hand is blackjack, check dealer hand to determine outcome
    elif blackjack_round.player_status is 'Blackjack':
        blackjack_round.dealer_hand.check_dealer_natural()
    # if neither, then initiate dealer sequence to determine outcome
    else:
        blackjack_round.dealer_sequence()
        # if dealer does not get a blackjack or bust, compare scores
        if blackjack_round.outcome is 'In Progress':
            pass
    # terminate round
    print('End of round!')
    return blackjack_round.outcome