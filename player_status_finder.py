from salary_raise import *
from transaction import DROP, PICKUP, TRADE

# Statuses
FREE_AGENT = "FREE_AGENT"
WAIVER_EXTENDABLE = "WAIVER_EXTENDABLE"
WAIVER_OUT_OF_CONTRACT = "WAIVER_OUT_OF_CONTRACT"
DRAFTED_OPTION = "DRAFTED_OPTION"
DRAFTED_OPTION_NOT_PICKED_UP = "DRAFTED_OPTION_NOT_PICKED_UP"
DRAFTED_EXTENDABLE = "DRAFTED_EXTENDABLE"
EXTENDED_EXTENDABLE = "EXTENDED_EXTENDABLE"
EXTENDED_END_OF_CONTRACT = "EXTENDED_END_OF_CONTRACT"

class PlayerStatusFinder:
    def __init__(self, playerName, position):
        self.playerName = playerName
        self.position = position

    """ Returns (status, yearDrafted, twoYearsAgoCost, oneYearAgoCost) """
    def findStatus(self, currentYear, keepers, oneYearAgoTransactions, twoYearsAgoTransactions, threeYearsAgoTransactions, oneYearAgoDraft, twoYearsAgoDraft, threeYearsAgoDraft):
        transaction = self.findTransaction(oneYearAgoTransactions)
        if transaction is not None:
            status = self.statusForTransaction(transaction, 1)
            return (self.statusRepresentation(status), "", "", transaction.amount)
        draft = self.findDraft(oneYearAgoDraft)
        if draft is not None:
            status = self.statusForDraft(draft, 1, keepers)
            return (self.statusRepresentation(status), str(currentYear - 1), "", draft.amount)

        transaction = self.findTransaction(twoYearsAgoTransactions)
        if transaction is not None:
            status = self.statusForTransaction(transaction, 2)
            return (self.statusRepresentation(status), "", transaction.amount, applyOneYearExtensionRaise(transaction.amount))
        draft = self.findDraft(twoYearsAgoDraft)
        if draft is not None:
            status = self.statusForDraft(draft, 2, keepers)
            return (self.statusRepresentation(status), str(currentYear - 2), draft.amount, applyOptionPickedUpRaise(draft.amount))

        transaction = self.findTransaction(threeYearsAgoTransactions)
        if transaction is not None:
            status = self.statusForTransaction(transaction, 3)
            raise Exception("Fail", "Cannot have most recent waiver pickup be 3 years ago")
        draft = self.findDraft(threeYearsAgoDraft)
        if draft is not None:
            status = self.statusForDraft(draft, 3, keepers)
            raise Exception("Fail", "Need to implement one/two year extension differentiation")

    """ Transactions must be sorted! """
    def findTransaction(self, transactions):
        if transactions is None:
            return None
        for transaction in transactions:
            # Ignore trades - they don't affect contracts.
            if transaction.playerName == self.playerName and transaction.position == self.position and transaction.transactionType != TRADE:
                return transaction
        return None

    def findDraft(self, draftEntries):
        if draftEntries is None:
            return None
        for draftEntry in draftEntries:
            if draftEntry.playerName == self.playerName and draftEntry.position == self.position:
                return draftEntry
        return None

    def statusForTransaction(self, transaction, yearsAgo):
        if transaction.transactionType == DROP:
            return FREE_AGENT
        if transaction.transactionType == PICKUP:
            if yearsAgo == 1:
                return WAIVER_EXTENDABLE
            if yearsAgo == 2:
                return WAIVER_OUT_OF_CONTRACT
            raise Exception("Fail", "Unexpected years ago: " + str(yearsAgo))
        raise Exception("Fail", "Unexpected transaction type: " + transaction.transactionType)

    def statusForDraft(self, draftEntry, yearsAgo, keepers):
        if yearsAgo == 1:
            if draftEntry.playerName in keepers:
                return DRAFTED_OPTION
            else:
                return DRAFTED_OPTION_NOT_PICKED_UP
        if yearsAgo == 2:
            return DRAFTED_EXTENDABLE
        if yearsAgo == 3:
            return EXTENDED_EXTENDABLE
        raise Exception("Fail", "Unexpected years ago: " + str(yearsAgo))

    # Matches the Google Sheet.
    def statusRepresentation(self, status):
        if status == FREE_AGENT:
            return "Free Agent"
        if status == WAIVER_EXTENDABLE:
            return "Waiver Pickup"
        if status == WAIVER_OUT_OF_CONTRACT:
            return "Waiver Pickup (End of Contract)"
        if status == DRAFTED_OPTION:
            return "Drafted Player (Option)"
        if status == DRAFTED_OPTION_NOT_PICKED_UP:
            return "Drafted Player (Option Not Picked Up)"
        if status == DRAFTED_EXTENDABLE:
            return "Drafted Player (Extension)"
        if status == EXTENDED_EXTENDABLE:
            return "Extended Player (Extendable)"
        if status == EXTENDED_END_OF_CONTRACT:
            return "Extended Player (End of Contract)"