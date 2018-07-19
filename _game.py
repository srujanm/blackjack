"""
Blackjack game object
"""
class Game():
	def __init__(self, player_name='Human'):
		"""
		Attributes:
			player_name (str)
			no_rounds (int): number of rounds elapsed since start of game
			money (int): amount of money over all elapsed rounds. positive for net gain, negative for net loss
		"""
		# opening message
		print('Starting game!\n')
		self.player_name = player_name
		self.no_rounds = 0
		self.money = 0

	# def next_round(self):
	# 	"""Increments no_rounds"""
	# 	self.no_rounds += 1

	# def 