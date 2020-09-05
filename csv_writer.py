import csv

class CSVWriter:
	def __init__(self, teams):
		self.teams = teams

	def writeToCSV(self, filename):
		with open(filename, "w", newline="") as csvFile:
			writer = csv.writer(csvFile, delimiter=",")

			writer.writerow(["", "Position", "Status", "Year Drafted", "2018 Cost", "2019 Cost"])

			for team in self.teams:
				writer.writerow([team.name, team.owner])
				for player in team.players:
					writer.writerow([player.name, player.position, player.status, player.draftedYear, player.twoYearsAgoCost, player.oneYearAgoCost])
				writer.writerow([])
				writer.writerow([])