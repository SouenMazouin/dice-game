import random

class Dice:
    """
    Base class to represent a dice
    """
    def __init__(self, nbfaces):
        self.nbfaces = nbfaces

    def throwDice(self):
        """
        Throw the dice and returns a random number between 1 and the number of faces.
        """
        return random.randint(1, self.nbfaces)

class Dice_with_6_faces(Dice):
    """
    Class representing a dice with six faces.
    """
    def __init__(self):
        super().__init__(6)

class Dice_with_20_faces(Dice):
    """
    Class representing a dice with twenty faces.
    """
    def __init__(self):
        super().__init__(20)
