from dice_library.dice import Dice_with_6_faces, Dice_with_20_faces

def main():
    # Create a list of five dices with 6 faces and five dices with 20 faces
    dices = [Dice_with_6_faces() for _ in range(5)] + [Dice_with_20_faces() for _ in range(5)]

    # Throw all dices
    results = throwAllDicesFromList(dices)

    # Split the results into two lists
    dice_with_6_faces_results = []
    dice_with_20_faces_results = []

    for i in range(len(results)):
        if i < 5:
            dice_with_6_faces_results.append(results[i])
        else:
            dice_with_20_faces_results.append(results[i])

    # Check if the player has won or lost and display the results
    if checkForWin(dice_with_6_faces_results, dice_with_20_faces_results):
        print("---\nWin !!!")
    else:
        print("---\nLost :\\")


def throwAllDicesFromList(dices_list):
    """
    Throw all the dices in the list, prints the result of each throw, and returns a list of the results.
    """
    results = []
    for dice in dices_list:
        result = dice.throwDice()
        print(f"Result of {type(dice).__name__} : {result}")
        results.append(result)
    return results


def checkForWin(dice_with_6_faces_results, dice_with_20_faces_results):
    """
    Verifies if the player has won based on the results obtained.

    The player wins if he has obtained:
    - a pair with the dice with six sides
    - a 20 with a dice with twenty sides
    """
    # Convert the list of dice with 6 faces results to a set, which removes any duplicate values.
    has_pair = len(set(dice_with_6_faces_results)) < len(dice_with_6_faces_results)
    has_twenty = 20 in dice_with_20_faces_results

    return has_pair or has_twenty


if __name__ == "__main__":
    main()
