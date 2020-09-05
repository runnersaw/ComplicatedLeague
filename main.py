from csv_writer import CSVWriter
from canonical_name import canonicalName
from current_team_name import currentTeamName
from draft_loader import DraftLoader
from keepers_loader import KeepersLoader
from player import Player
from player_status_finder import PlayerStatusFinder
from team import Team
from team_loader import TeamLoader
from team_owner import teamOwner
from transaction_loader import TransactionLoader

if __name__=="__main__":
    currentYear = 2020

    transactionLoader = TransactionLoader()
    oneYearAgoTransactions = transactionLoader.load("data/transactions_2019.csv", 1)
    twoYearsAgoTransactions = transactionLoader.load("data/transactions_2018.csv", 2)

    draftLoader = DraftLoader()
    oneYearAgoDraft = draftLoader.load("data/draft_2019.csv", 1)
    twoYearsAgoDraft = draftLoader.load("data/draft_2018.csv", 2)

    keepersLoader = KeepersLoader()
    keepers = keepersLoader.load("data/keepers_2019.csv")

    teams = []
    teamLoader = TeamLoader()
    for teamName, playerNamePositions in teamLoader.load("data/teams_2020.csv"):
        owner = teamOwner(currentTeamName(canonicalName(teamName)))
        players = []
        for playerNamePosition in playerNamePositions:
            playerName = playerNamePosition[0]
            position = playerNamePosition[1]
            statusFinder = PlayerStatusFinder(canonicalName(playerName), position)
            result = statusFinder.findStatus(currentYear, keepers, oneYearAgoTransactions, twoYearsAgoTransactions, None, oneYearAgoDraft, twoYearsAgoDraft, None)
            if result is not None:
                status, draftedYear, twoYearsAgoCost, oneYearAgoCost = result
                players.append(Player(playerName, position, status, draftedYear, twoYearsAgoCost, oneYearAgoCost))
            else:
                raise Exception("Fail", "Missing player: " + playerName)
        teams.append(Team(teamName, owner, players))
    csvWriter = CSVWriter(teams)
    csvWriter.writeToCSV("out/status_2020.csv")

    while False:
        player = input("Player?\n")
        if player == "":
            break
        playerStatusFinder = PlayerStatusFinder(canonicalName(player))
        status = playerStatusFinder.findStatus(currentYear, keepers, oneYearAgoTransactions, twoYearsAgoTransactions, None, oneYearAgoDraft, twoYearsAgoDraft, None)
        statusRepresentation = playerStatusFinder.statusRepresentation(status)
        print(statusRepresentation)
