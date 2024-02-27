
class Player:
    def __init__(self, args: list, weights: list):
        self.name = args[0]
        self.desirability = float(args[1])
        self.technical = float(args[2])
        self.physical = float(args[3])
    
        # Weights: Desirability, technical, physical
        self.weights = weights
        
    
    def getScore(self):
        return self.desirability * self.weights[0] + self.technical * self.weights[1] + self.physical * self.weights[2]
    
def teamScore(team: list[Player]) -> int:
    score = 0
    for player in team:
        score += player.getScore()
        
    return score