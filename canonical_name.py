
# Converts a player or team name to an easily comparible form.
def canonicalName(name):
    return name.upper().replace(".", "").replace("'", "").replace("&AMP;", "&")