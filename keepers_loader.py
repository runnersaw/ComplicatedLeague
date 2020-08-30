import csv
from canonical_name import canonicalName

class KeepersLoader():
    def __init__(self):
        pass

    def load(self, filename):
        keepers = []
        with open(filename) as csvFile:
            reader = csv.reader(csvFile, delimiter=",")

            for row in reader:
                if row is None:
                    continue
                if len(row) < 1:
                    raise Exception("Fail", "Expected row of length 1, got: " + row)
                keeper = canonicalName(row[0])
                keepers.append(keeper)

        return keepers
