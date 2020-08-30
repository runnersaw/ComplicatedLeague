

class DraftEntry:
    def __init__(self, playerName, teamName, amount):
        self.playerName = playerName
        self.teamName = teamName
        self.amount = amount

    def __repr__(self):
        return self.playerName + " drafted by " + self.teamName + " for " + str(self.amount)