from transaction import Transaction

class UnresolvedPlayer:
	def __init__(self, name, position):
		self.name = name
		self.position = position

class RawTransaction:
	def __init__(self, type, amount, year, playerName):
		self.transaction = Transaction(type, amount, year)
		self.playerName = playerName

class PlayerResolver:
	def __init__(self):
		pass

	def resolve(self, unresolvedPlayers, rawTransactions):
		return []