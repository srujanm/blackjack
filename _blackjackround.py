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
    round = Round(player_name)
    # initiate player sequence
    round.player_sequence()
    """after player sequence"""
    # if player hand is bust, just go ahead and terminate round
    if round.player_status == 'Bust':
        pass
    # if player hand is blackjack, check dealer hand to determine outcome
    elif round.player_status == 'Blackjack':
        round.check_dealer_natural()
    # if neither, then initiate dealer sequence to determine outcome
    else:
        round.dealer_sequence()
        # if dealer does not get a blackjack or bust, compare scores
        if round.outcome == 'In Progress':
            round.compare_scores()
    # terminate round
    print('\nEnd of round!')
    return round.outcome