import pyperclip
from csv_writer import CSVWriter
from canonical_name import canonicalName
from draft_loader import DraftLoader
from keepers_loader import KeepersLoader
from player_status_finder import PlayerStatusFinder
from team_loader import TeamLoader
from transaction_loader import TransactionLoader

if __name__=="__main__":
    transactionLoader = TransactionLoader()
    oneYearAgoTransactions = transactionLoader.load("data/transactions_2019.csv", 1)
    twoYearsAgoTransactions = transactionLoader.load("data/transactions_2018.csv", 2)

    draftLoader = DraftLoader()
    oneYearAgoDraft = draftLoader.load("data/draft_2019.csv", 1)
    twoYearsAgoDraft = draftLoader.load("data/draft_2018.csv", 2)

    keepersLoader = KeepersLoader()
    keepers = keepersLoader.load("data/keepers_2019.csv")

    teamLoader = TeamLoader()
    print(teamLoader.load("data/teams_2020.csv"))

    while True:
        player = input("Player?\n")
        if player == "":
            break
        playerStatusFinder = PlayerStatusFinder(canonicalName(player))
        status = playerStatusFinder.findStatus(keepers, oneYearAgoTransactions, twoYearsAgoTransactions, None, oneYearAgoDraft, twoYearsAgoDraft, None)
        statusRepresentation = playerStatusFinder.statusRepresentation(status)
        print(statusRepresentation)

        pyperclip.copy(statusRepresentation)
