from utils.textFormatting import background, style, color

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def error():
    """
    Generates a message with a red color indicating "Invalid. Try again." and
    resets the color to white.

    """

    message = background(40) + style(0) + color(31) + \
              "Invalid. Try again.\n" + \
              background(40) + style(0) + color(37)
    print(message)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
def getDesireWeight():
    """
    Prompts the user to input a weight for desire to play and ensures that the
    input is a numeric value.
    
    Returns
    -------
    The weight for desire to play
    
    """

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
    """
    Prompts the user to input a weight for technical ability and ensures that
    the input is a numeric value.
    
    Returns
    -------
    The weight for technical ability
    
    """
    
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
    """
    Prompts the user to input a weight for physical ability and ensures that
    the input is a numeric value.
    
    Returns
    -------
    The weight for physical ability
    
    """
    
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

prompt = background(40) + style(0) + color(36) + \
         "Would you like to change these weights? [y / n]" + \
         background(40) + style(0) + color(37)
              


def setup():
    """
    Prompts the user to change weights and returns normalized weights if the
    user chooses to change them, otherwise it returns default weights:

    * Desire to play: 0.4
    * Technical ability: 0.35
    * Physical ability: 0.25
    
    Return
    ------
    A list of weights
    
    """

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
        import numpy as np
        return np.array(weights) / sum(weights)
    
    else:
        return 0.4, 0.35, 0.25