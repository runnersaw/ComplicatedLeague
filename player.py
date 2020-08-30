from transaction import Transaction

class Player:
	def __init__(self, name, position, transaction):
		self.name = name
		self.position = position
		self.transaction = transaction

	def updateTransaction(self, transaction):
		self.transaction = transaction

