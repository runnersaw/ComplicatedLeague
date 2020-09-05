import csv
import re
from canonical_name import canonicalName
from current_team_name import currentTeamName
from transaction import Transaction, DROP, PICKUP, TRADE

class TransactionLoader():
    def __init__(self):
        pass

    def load(self, filename, yearsAgo):
        transactions = []
        with open(filename) as csvFile:
            reader = csv.reader(csvFile, delimiter=",")

            for row in reader:
                if row is None:
                    continue
                if len(row) < 3:
                    raise Exception("Fail", "Expected row of length 3, got: " + row)
                result = self.parseTransaction(row[3])
                if result is None:
                    continue
                transactionType, amount = result
                playerName = canonicalName(row[1])
                position = row[2]
                teamName = currentTeamName(canonicalName(row[0]))
                transaction = Transaction(playerName, position, teamName, transactionType, amount, yearsAgo)
                transactions.append(transaction)

        return transactions

    def parseTransaction(self, transaction):
        pickupMatch = re.search("Won at \\$(\\d+)", transaction)
        if pickupMatch is not None:
            amount = int(pickupMatch.group(1))
            return (PICKUP, amount)

        if transaction == "Dropped":
            return (DROP, 0)

        tradedMatch = re.search("Traded From (.*)", transaction)
        if tradedMatch is not None:
            return (TRADE, 0)

        raise Exception("Fail", "Failed to parse transaction: " + transaction)