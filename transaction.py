

# Possible transaction types.
DRAFT = "DRAFT"
PICKUP = "PICKUP"
DROP = "DROP"

# Possible statuses
WAIVER_PICKUP = "Waiver Pickup"
DRAFT_OPTION = "Drafted Player (Option)"
DRAFT_EXTENSION = "Drafted Player (Extension)"

def validateType(type):
	if not isinstance(type, str):
		raise Exception("Fail", "Unexpected type: " + type) 
	if type != DRAFT and type != PICKUP and type != DROP:
		raise Exception("Fail", "Unexpected transaction type: " + type)

class Transaction:
	def __init__(self, type, amount, year):
		validateType(type)
		self.type = type
		self.amount = amount
		self.year = year

	def currentStatus(self):
		# TODO
		return WAIVER_PICKUP

	def draftedYear(self):
		return None