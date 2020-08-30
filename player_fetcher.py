from player_resolver import UnresolvedPlayer, RawTransaction, PlayerResolver
from transaction import Transaction, DRAFT

class PlayerFetcher:
	def __init__(self):
		pass

	def fetch(self):
		unresolvedPlayers = [
			UnresolvedPlayer("Andy Dalton", "QB"),
			UnresolvedPlayer("Drew Brees", "QB"),
		]
		rawTransactions = [
			RawTransaction(DRAFT, "0", 2019, "Drew Brees")
		]
		resolver = PlayerResolver()
		players = resolver.resolve(unresolvedPlayers, rawTransactions)
		return players