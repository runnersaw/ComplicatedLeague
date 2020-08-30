

# Possible transaction types.
PICKUP = "PICKUP"
DROP = "DROP"
TRADE = "TRADE"

def validateType(transactionType):
	if not isinstance(transactionType, str):
		raise Exception("Fail", "Unexpected type: " + transactionType)
	if transactionType != PICKUP and transactionType != DROP and transactionType != TRADE:
		raise Exception("Fail", "Unexpected transaction type: " + transactionType)

class Transaction:
	def __init__(self, playerName, teamName, transactionType, amount, yearsAgo):
		self.playerName = playerName
		self.teamName = teamName
		validateType(transactionType)
		self.transactionType = transactionType
		self.amount = amount
		if yearsAgo < 1 or yearsAgo > 3:
			raise Exception("Invalid yearsAgo: " + str(yearsAgo))
		self.yearsAgo = yearsAgo

	def __repr__(self):
		return "Transaction: " + self.playerName + " had " + self.transactionType + " at amount " + str(self.amount) + " to " + self.teamName
