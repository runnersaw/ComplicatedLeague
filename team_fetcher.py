from player import Player
from player_fetcher import PlayerFetcher
from team import Team
from transaction import Transaction, DRAFT

class TeamFetcher:
	def __init__(self):
		self.playerFetcher = PlayerFetcher()

	def fetch(self):
		players = self.playerFetcher.fetch()

		teams = [
			Team("Mine", "Sawyer", players),
			Team("Yours", "His", players),
		]

		return teams