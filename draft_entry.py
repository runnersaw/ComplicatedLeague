

class DraftEntry:
    def __init__(self, playerName, position, teamName, amount):
        self.playerName = playerName
        self.position = position
        self.teamName = teamName
        self.amount = amount

    def __repr__(self):
        return self.playerName + "-" + self.position + " drafted by " + self.teamName + " for " + str(self.amount)