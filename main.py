from utils.textFormatting import background, style, color
from lib.player import teamScore
from lib.roster import getRoster

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# The more you shuffle, the probability that the teams are similar in score
# increases, but the chance that the same teams happen every time is larger.

def sorting(file, new_shuffles):  # sourcery skip: extract-duplicate-method
    shuffles = 60
    if new_shuffles != None and new_shuffles.isnumeric():
        shuffles = int(new_shuffles)
        
    roster = getRoster(file)

    # Separate the teams to start
    team1 = roster[:len(roster)//2]
    team2 = roster[len(roster)//2:]
    teams = team1.copy(), team2.copy()

    # Get difference
    least_diff = abs(teamScore(team1) - teamScore(team2))

    # Keep trying to minimize the difference, and when it happens, save
    # formation
    import random
    for _ in range(shuffles):
        team1, team2 = [], []
        random.shuffle(roster)
        
        team1 = roster[:len(roster)//2]
        team2 = roster[len(roster)//2:]

        team1_score = teamScore(team1)
        team2_score = teamScore(team2)

        if abs(team1_score - team2_score) < least_diff:
            least_diff = abs(team1_score - team2_score)
            teams = team1.copy(), team2.copy()
        

    out = background(40) + style(0) + color(32) + \
          "\nFinal formation has been found." + \
          background(40) + style(0) + color(37)
    print(out, end='\n')

    print(f"The teams differ by {round(least_diff, 4)}.", end='\n\n')
    

    out = background(46) + style(1) + color(37) + \
          f"TEAM 1:\t\t{str(round(teamScore(teams[0]),4))}" + \
          background(40) + style(0) + color(37)
    print(out, end='\n')
    for player in teams[0]:
        out = player.name + '\t\t' + \
              background(46) + style(0) + color(37) + \
              str(round(player.getScore(), 4)) + \
              background(40) + style(0) + color(37)
        print(out)
    print()


    out = background(46) + style(1) + color(37) + \
          f"TEAM 2:\t\t{str(round(teamScore(teams[1]),4))}" + \
          background(40) + style(0) + color(37)
    print(out, end='\n')
    for player in teams[1]:
        out = player.name + '\t\t' + \
              background(44) + style(0) + color(37) + \
              str(round(player.getScore(), 4)) + \
              background(40) + style(0) + color(37)
        print(out)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def main(filename, shuffles):
    sorting(filename if filename != None else "data/example.csv", shuffles)
        
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Filename')
    parser.add_argument('--filename', metavar='path', required=False)
    parser.add_argument('--shuffles', metavar='path', required=False)
    args = parser.parse_args()
    main(filename=args.filename, shuffles=args.shuffles)