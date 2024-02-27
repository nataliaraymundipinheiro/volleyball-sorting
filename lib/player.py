class Player:
    """
    Represents a player in the volleyball game.
    """

    def __init__(self, args: list, weights: list):
        """
        Initializes an object with attributes based on input arguments and
        weights.
        
        Parameters
        ----------
        args: List containing the following elements in order: name, desire to
            play, technical ability, and physical ability

        weights: List of weights for the different attributes. These weights are
            used to calculate a weighted sum (score) of the attributes for a
            particular player

        """

        self.name = args[0]
        self.desire = float(args[1])
        self.technical = float(args[2])
        self.physical = float(args[3])
    
        # Weights: desire, technical, physical
        self.weights = weights
        
    
    def getScore(self):
        """
        Calculates a score based on the desire to play, technical ability, and
        physical ability of a player using corresponding weights.
        
        Returns
        -------
        The player score

        """

        return self.desire    * self.weights[0] + \
               self.technical * self.weights[1] + \
               self.physical  * self.weights[2]
    

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def teamScore(team: list[Player]) -> int:
    """
    Calculates the total score of a team based on the scores of its players.
    
    Parameters
    ----------
    team: A list of Player objects representing a team. 

    Returns
    -------
    The total score of a team

    """
    
    return sum(player.getScore() for player in team)