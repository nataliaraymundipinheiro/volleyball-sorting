from utils.textFormatting import ANSI
import numpy as np
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def error():
    message = ANSI.background(40) + ANSI.style(0) + ANSI.color(31) + \
              "Invalid. Try again.\n" + \
              ANSI.background(40) + ANSI.style(0) + ANSI.color(37)
    print(message)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
def getDesireWeight():
    def out():
        print("Desire to play:", end='\t\t')
    
    out()
    stream = input()
    while not stream.isnumeric():
        error()
        out()
        stream = input()

    return abs(float(stream))


def getTechnicalWeight():
    def out():
        print("Technical ability:", end='\t')
    
    out()
    stream = input()
    while not stream.isnumeric():
        error()
        out()
        stream = input()

    return abs(float(stream))


def getPhysicalWeight():
    def out():
        print("Physical ability:", end='\t')

    out()    
    stream = input()
    while not stream.isnumeric():
        error()
        out()
        stream = input()

    return abs(float(stream))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def getWeights():
    return getDesireWeight(), getTechnicalWeight(), getPhysicalWeight()
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

introduction = """
--------------------------------------------------------------------------------
Welcome to the volleyball sorting algorithm!

Given 12 players, we sort two teams based on each player's desire to play,
technical abilities, and physical abilities. You will be prompted to select the
weights for each category. You can choose to use the default settings, where the
weights are

* Desire to play: 40%
* Technical ability: 35%
* Physical ability: 25%

"""

prompt = ANSI.background(40) + ANSI.style(0) + ANSI.color(36) + \
         "Would you like to change these weights? [y / n]" + \
         ANSI.background(40) + ANSI.style(0) + ANSI.color(37)
              


def setup():
    # Print introduction text
    # This will prompt the user if they want to change the weights
    print(introduction + prompt, end='\t')
    stream = input() # Change the weights? [y / n]
    
    # Answer must be 'y' or 'n', otherwise keep prompting user
    while stream != 'y' and stream != 'n':
        error() # Print error message
        print(prompt, end='\t')
        stream = input()

    if stream == 'y':
        weights = getWeights()
        return np.array(weights) / sum(weights)
    else:
        return 0.4, 0.35, 0.25