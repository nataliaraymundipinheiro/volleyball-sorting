from utils.textFormatting import background, style, color
from lib.player import Player, teamScore
from lib.setup import setup

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def readFile(file):
    """
    Reads a CSV file, skips the header row, and returns the remaining rows as a 
    list.
    
    Parameters
    ----------
    file: Name or path of the file to be read
    
    Returns
    -------
    List of rows from the file, excluding the header row
    
    """
    
    file = open(file, "r")
    
    # Read file and skip header
    import csv
    csvreader = csv.reader(file)
    next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    file.close()

    return rows

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def checkRoster(players):
    """
    Checks the number of players in a roster and prints a message if it is
    insufficient or too many, and then exits the code.
    
    Parameters
    ----------
    players: Players in a roster
    
    """

    if len(players) < 12:
        out = background(40) + style(0) + color(31) + \
              "Insufficient number of players." + \
              background(40) + style(0) + color(37)
        print(out)
        exit()
        
    elif len(players) > 12:
        out = background(40) + style(0) + color(31) + \
              "Too many players." + \
              background(40) + style(0) + color(37)
        print(out)
        exit()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def getRoster(file):
    """
    Reads a file, checks the roster, sets up weights, and transforms the data
    into a list of Player objects.
    
    Parameters
    ----------
    file: A file path that contains the roster information in CSV format

    Returns
    -------
    A list of Player objects created from the data in the input file

    """

    file = readFile(file)
    checkRoster(file)

    # Get weights
    weights = setup()

    # Transform the csv into a list of Player objects
    roster = []
    for player in file:
        roster.append(Player(player, weights))

    return roster