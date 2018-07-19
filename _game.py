"""
Blackjack game object
"""
from ._blackjackround import blackjack_round

class Game():
    def __init__(self):
        """
        Attributes:
            player_name (str)
            no_rounds (int): number of rounds elapsed since start of game
            money (int): amount of money over all elapsed rounds. positive for net gain, negative for net loss
        """
        # opening message
        print('Enter your name!')
        self.player_name = input()
        self.no_rounds = 0
        self.money = 0

    def set_money(self):
        print('How much money do you want to put on the table? ;)')
        self.money = request_int()

    def adjust_winings(self, round_outcome):
        """
        Method to adjust winnings after a round
        Inputs:
            round_outcome (str): 'Win', 'Loss' or 'Draw'
        """
        ### TO ADD ###
        pass

    def request_round():
        """
        Function which checks validity of player input while requesting if they want a new round
        Returns:
            (str)
        """
        print('\nDo you want to start a round? y or n')
        while True:
            answer = input()
            # check for validity of input
            if answer != 'y' and answer != 'n':
                print('Invalid input! Try again')
                continue
            else:
                break
        return answer 

    def start_game(self):
        """"Main method that implements game"""
        # opening message
        print('\nStarting new game!')
        # ask player for money to put on the table
        self.set_money() ### CANT FIND REQUEST_INT for some reason
        # initialize game loop
        while True:
            # see if the player wants a new round
            player_input = request_round()
            # if player says no, exit game loop
            if player_input == 'n':
                break
            # if player says yes, play new round
            elif player_input == 'y':
                # accept bet input
                round_bet = request_bet()
                # initiate round
                #round_outcome = blackjack_round()
                # adjust winnings based on round outcome
                self.adjust_winings(round_outcome)
            # if player entered wrong input, do nothing
            else:
                pass

def request_int():
    """
    Function which checks validity of player input while requesting an integer
    Returns:
        (int)
    """
    while True:
        try:
            amount = float(input())
            break
        except ValueError:
            print('Invalid input! You must enter a number')
    return amount
            
def request_bet():
    """
    Function which checks validity of player input while requesting bet amount in a round
    Returns:
        (int)
    """
    ### TO ADD ###
    pass