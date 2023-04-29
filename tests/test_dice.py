from dice_library.dice import Dice_with_6_faces, Dice_with_20_faces
from main import throwAllDicesFromList, checkForWin 

def test_throwAllDicesFromList():
    dice_with_6_faces = Dice_with_6_faces()
    assert 1 <= throwAllDicesFromList([dice_with_6_faces])[0] <= 6 # check if the result is between 1 and 6

    dice_with_20_faces = Dice_with_20_faces()
    assert 1 <= throwAllDicesFromList([dice_with_20_faces])[0] <= 20 # check if the result is between 1 and 20

def test_checkForWin():
    assert checkForWin([1, 1, 3, 4, 5], [20, 2, 3, 4, 5])  # a pair in the dices with six faces and 20 in a dice with twennty faces
    assert not checkForWin([1, 2, 3, 4, 5], [19, 2, 3, 4, 5])  # no pair and no 20
    assert checkForWin([1, 1, 3, 4, 5], [19, 2, 3, 4, 5])  # a pair in the dices with six faces
    assert checkForWin([1, 2, 3, 4, 5], [20, 2, 3, 4, 5])  # 20 in a dice with twenty faces
    
def test_dice_with_6_faces():
    dice = Dice_with_6_faces()
    assert 1 <= dice.throwDice() <= 6 # check if the result is between 1 and 6 with the trow method

def test_dice_with_20_faces():
    dice = Dice_with_20_faces()
    assert 1 <= dice.throwDice() <= 20 # check if the result is between 1 and 20 with the trow method
