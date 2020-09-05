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
    oneYearAgoTransactions = transactionLoader.load("data/transactions_" + str(currentYear - 1) + ".csv", 1)
    twoYearsAgoTransactions = transactionLoader.load("data/transactions_" + str(currentYear - 2) + ".csv", 2)

    draftLoader = DraftLoader()
    oneYearAgoDraft = draftLoader.load("data/draft_" + str(currentYear - 1) + ".csv")
    twoYearsAgoDraft = draftLoader.load("data/draft_" + str(currentYear - 2) + ".csv")

    keepersLoader = KeepersLoader()
    keepers = keepersLoader.load("data/keepers_" + str(currentYear - 1) + ".csv")

    teams = []
    teamLoader = TeamLoader()
    for teamName, playerNamePositions in teamLoader.load("data/teams_" + str(currentYear) + ".csv"):
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
    csvWriter = CSVWriter(teams, currentYear)
    csvWriter.writeToCSV("out/status_" + str(currentYear) + ".csv")

    while False:
        player = input("Player?\n")
        if player == "":
            break
        playerStatusFinder = PlayerStatusFinder(canonicalName(player))
        status = playerStatusFinder.findStatus(currentYear, keepers, oneYearAgoTransactions, twoYearsAgoTransactions, None, oneYearAgoDraft, twoYearsAgoDraft, None)
        statusRepresentation = playerStatusFinder.statusRepresentation(status)
        print(statusRepresentation)
