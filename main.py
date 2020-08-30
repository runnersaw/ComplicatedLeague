from csv_writer import CSVWriter
from team_fetcher import TeamFetcher

if __name__=="__main__":
	teamFetcher = TeamFetcher()
	teams = teamFetcher.fetch()

	writer = CSVWriter(teams)
	writer.writeToCSV("data/data.csv")
