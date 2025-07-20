'''A round-robin tournament is one in which each team competes with every other team. Consider a version of the IPL tournamentin which every team plays exactly one game
against every other team. All these games have a definite result and no match ends in a tie. The winning team in each match is awarded one point.

Eight teams participate in this round-robin cricket tournament: CSK, DC, KKR, MI, PK, RR, RCB and SH. You are given the details of the outcome of the matches. Your 
task is to prepare the IPL points table in descending order of wins. If two teams have the same number of points, the team whose name comes first in alphabetical order 
must figure higher up in the table.

There are eight lines of input. Each line is a sequence of comma-separated team names. The first team across these eight lines will always be in this order: CSK, DC, 
KKR, MI, PK, RR, RCB and SH. For a given sequence, all the other terms represent the teams that have lost to the first team. For example, the first line of input 
could be: CSK,MI,DC,PK. This means that CSK has won its matches against the teams MI, DC and PK and lost its matches against all other teams. If a sequence has just 
one team, it means that it lost all its matches.

Print the IPL points table in the following format — team:wins — one team on each line. There shouldn't be any spaces in any of the lines'''

def prepare_points_table():
    # List of teams in order
    teams = ["CSK", "DC", "KKR", "MI", "PK", "RR", "RCB", "SH"]
    # Dictionary to store wins for each team
    points_table = {team: 0 for team in teams}

    # Read input for each team's match outcomes
    for i in range(8):
        match_outcome = input().strip().split(",")
        # First element is the team name
        team = match_outcome[0]
        # Remaining elements are the teams that this team defeated
        wins = match_outcome[1:]
        points_table[team] += len(wins)  # Add the number of wins for this team
        # Increment wins for each team that lost to the current team
        for opponent in wins:
            points_table[opponent] += 0  # Opponent lost, no increment needed

    # Sort the points table by number of wins (descending) and by team name (alphabetical)
    sorted_table = sorted(points_table.items(), key=lambda x: (-x[1], x[0]))

    # Print the sorted points table in the required format
    for team, wins in sorted_table:
        print(f"{team}:{wins}")

# Call the function to execute
prepare_points_table()