import csv
from canonical_name import canonicalName
from current_team_name import currentTeamName

class TeamLoader():
    def __init__(self):
        pass

    """ Does NOT return canonical names or updated team names """
    def load(self, filename):
        teams = []
        with open(filename) as csvFile:
            reader = csv.reader(csvFile, delimiter=",")

            for row in reader:
                if row is None:
                    continue
                if len(row) < 2:
                    raise Exception("Fail", "Expected row of length 1, got: " + row)
                teamName = row[0]
                players = []
                for i in range (1, len(row)):
                    playerName = row[i].split("~")[0]
                    position = row[i].split("~")[1]
                    players.append((playerName, position))
                teams.append((teamName, players))

        return teams
