from utils.readFile import readFile
from utils.textFormatting import ANSI
from lib.player import Player, teamScore
from lib.setup import setup

import random
import numpy as np

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# The more you shuffle, the probability that the teams are similar in score
# increases, but the chance that the same teams happen every time is larger.
shuffles = 60

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def checkRoster(players):
    if len(players) < 12:
        out = ANSI.background(40) + ANSI.style(0) + ANSI.color(31) + \
              "Insufficient number of players." + \
              ANSI.background(40) + ANSI.style(0) + ANSI.color(37)
        print(out)
        return -1
        
    elif len(players) > 12:
        out = ANSI.background(40) + ANSI.style(0) + ANSI.color(31) + \
              "Too many players." + \
              ANSI.background(40) + ANSI.style(0) + ANSI.color(37)
        print(out)
        return -1

    return 0
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def sorting(file):
    players = readFile(file)
    if checkRoster(players) == -1: return -1

    # Get weights
    weights = setup()

    # Transform the csv into a list of Player objects
    roster = []
    for player in players:
        roster.append(Player(player, weights))

    # Separate the teams to start
    team1 = roster[:len(roster)//2]
    team2 = roster[len(roster)//2:]
    teams = team1.copy(), team2.copy()

    # Get difference
    least_diff = abs(teamScore(team1) - teamScore(team2))

    # Keep trying to minimize the difference, and when it happens, save
    # formation
    for i in range(shuffles):
        team1, team2 = [], []
        random.shuffle(roster)
        
        team1 = roster[:len(roster)//2]
        team2 = roster[len(roster)//2:]

        team1_score = teamScore(team1)
        team2_score = teamScore(team2)

        if abs(team1_score - team2_score) < least_diff:
            least_diff = abs(team1_score - team2_score)
            teams = team1.copy(), team2.copy()
        

    out = ANSI.background(40) + ANSI.style(0) + ANSI.color(32) + \
          "\nFinal formation has been found." + \
          ANSI.background(40) + ANSI.style(0) + ANSI.color(37)
    print(out, end='\n\n')

    print(f"The teams differ by {round(least_diff, 4)}", end='\n\n')
    

    out = ANSI.background(46) + ANSI.style(1) + ANSI.color(37) + \
          f"TEAM 1:\t\t{str(round(teamScore(teams[0]),4))}" + \
          ANSI.background(40) + ANSI.style(0) + ANSI.color(37)
    print(out, end='\n')
    for player in teams[0]:
        out = player.name + '\t\t' + \
              ANSI.background(46) + ANSI.style(0) + ANSI.color(37) + \
              str(round(player.getScore(), 4)) + \
              ANSI.background(40) + ANSI.style(0) + ANSI.color(37)
        print(out)
    print()


    out = ANSI.background(46) + ANSI.style(1) + ANSI.color(37) + \
          f"TEAM 2:\t\t{str(round(teamScore(teams[1]),4))}" + \
          ANSI.background(40) + ANSI.style(0) + ANSI.color(37)
    print(out, end='\n')
    for player in teams[1]:
        out = player.name + '\t\t' + \
              ANSI.background(44) + ANSI.style(0) + ANSI.color(37) + \
              str(round(player.getScore(), 4)) + \
              ANSI.background(40) + ANSI.style(0) + ANSI.color(37)
        print(out)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def main():
    sorting("data/players.csv")


if __name__ == "__main__":
    main()