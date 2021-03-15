WS_List = open("WorldSeriesWinners.txt", "r")

year = int(input("Select a year from 1903 to 2008: "))

while year == 1904 or year == 1994 or year > 2008:
    year = int(input("No World Series Played this year. Select another : "))
winner = WS_List.read()
winner = winner.split("\n")

# 1st Dictionary Requirement
years_won = {}
year = 1903
for team in winner:
    years_won[year] = team
    if year != 1903 or year != 1993:
        year += 1
    else:
        year += 2

# 2nd Dictionary Requirement
total_won = {}
for team in winner:
    total_won[team] = total_won.get(team, 0) + 1

# Final Output
print(
    "In",
    year,
    ": The",
    years_won[year],
    "won. They have won",
    total_won[years_won[year]],
    "total World Series.",
)
