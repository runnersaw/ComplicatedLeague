from transaction import Transaction

class Player:
    def __init__(self, name, position, status, draftedYear, twoYearsAgoCost, oneYearAgoCost):
        self.name = name
        self.position = position
        self.status = status
        self.draftedYear = draftedYear
        self.twoYearsAgoCost = twoYearsAgoCost
        self.oneYearAgoCost = oneYearAgoCost

