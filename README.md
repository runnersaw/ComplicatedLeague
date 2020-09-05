# Complicated League

Data and code related to maintaining the complicated keeper IDP league.

## Pre-Year Keeper Sheet Setup

1. Open the [Google Sheet](https://docs.google.com/spreadsheets/d/1VXdzBVnzW5Z_ryyd6sAKFD9FRWKi2Rjbs05c4gH7xyc/edit).
1. Make a copy of the "Year X Pre-Year Keepers Template".
1. Run the commands in `data/commands.txt` to gather `draft_20XX.csv`, `transactions_20XX.csv`, and `teams_20XX.csv` for the previous year.
1. Create `keepers_20XX.csv` for the current year for players with options picked up.
1. Update `TEAM_NAME_MAP` in `current_team_name.py` if necessary.
1. Update `currentYear` in `main.py`.
1. Run `main.py`!