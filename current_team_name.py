
# The dictionary from every name a team has had to its current name.
# Canonical names only.
TEAM_NAME_MAP = {
    # Current names - 8/30/2020
    "DONALDS DUCKS": "DONALDS DUCKS",
    "BYE WEEK": "BYE WEEK",
    "2 GURLEYS 1 KUPP": "2 GURLEYS 1 KUPP",
    "FAMOUS AMOS": "FAMOUS AMOS",
    "FLOWERS & FLOWERS": "FLOWERS & FLOWERS",
    "FUCK YOU MELVIN JUST PLAY": "FUCK YOU MELVIN JUST PLAY",
    "PEACOCKS": "PEACOCKS",
    "PLACEHOLDER": "PLACEHOLDER",
    "SKEET BALL": "SKEET BALL",
    "TEAM SUZY": "TEAM SUZY",
    "THE TANK": "THE TANK",
    "VETERAN MINIMUM": "VETERAN MINIMUM",

    # Previous names
    # Find the links on the transactions page.
    # http://complicatedleague.football.cbssports.com/transactions/2018/all/all_but_lineup?pageIndex-tableContainer-0=-999
    "FUCK YOU LEVEON JUST PLAY": "FUCK YOU MELVIN JUST PLAY",
    "ODELL BECKHAM JESUS": "BYE WEEK",
    "ITS COMPLICATED": "DONALDS DUCKS",
    "2017 CLEVELAND BROWNS": "FAMOUS AMOS",
    "GARROPOYOLO": "FLOWERS & FLOWERS",
}

def currentTeamName(teamName):
    newName = TEAM_NAME_MAP[teamName]
    if newName is None:
        raise Exception("Unexpected team name: " + teamName)
    return newName