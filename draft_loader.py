import csv
from canonical_name import canonicalName
from current_team_name import currentTeamName
from draft_entry import DraftEntry

class DraftLoader():
    def __init__(self):
        pass

    def load(self, filename):
        draftEntries = []
        with open(filename) as csvFile:
            reader = csv.reader(csvFile, delimiter=",")

            for row in reader:
                if row is None:
                    continue
                if len(row) < 4:
                    raise Exception("Fail", "Expected row of length 4, got: " + row)
                playerName = canonicalName(row[1])
                position = row[2]
                teamName = currentTeamName(canonicalName(row[0]))
                amount = int(row[3])
                draftEntry = DraftEntry(playerName, position, teamName, amount)
                draftEntries.append(draftEntry)

        return draftEntries
