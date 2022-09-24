import random


def roll():
    
    dice_drawing = {
            1: """  
        _________
        |       |
        |   o   |
        |       |
        ---------
        """,
            2: """  
        _________
        |o      |
        |       |
        |      o|
        ---------""",
            3: """ 
        _________
        |o      |
        |   o   |
        |      o|
        ---------""",
            4: """
        _________
        |o     o|
        |       |
        |o     o|
        ---------""",
            5: """  
        _________
        |o     o|
        |   o   |
        |o     o|
        ---------""",
            6: """  
        _________
        |o     o|
        |o     o|
        |o     o|
        ---------
        """
    }
    
    print("Rolling the dice...")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    print("Dice rolled: {} and {}".format(dice1, dice2))
    
    match dice1, dice2:
        case 1, 1:
            print(dice_drawing[1])
            print(dice_drawing[1])
        case 1, 2:
            print(dice_drawing[1])
            print(dice_drawing[2])
        case 1, 3:
            print(dice_drawing[1])
            print(dice_drawing[3])
        case 1, 4:
            print(dice_drawing[1])
            print(dice_drawing[4])
        case 1, 5:
            print(dice_drawing[1])
            print(dice_drawing[5])
        case 1, 6:
            print(dice_drawing[1])
            print(dice_drawing[6])
        case 2, 1:
            print(dice_drawing[2])
            print(dice_drawing[1])
        case 2, 2:
            print(dice_drawing[2])
            print(dice_drawing[2])
        case 2, 3:
            print(dice_drawing[2])
            print(dice_drawing[3])
        case 2, 4:
            print(dice_drawing[2])
            print(dice_drawing[4])
        case 2, 5:
            print(dice_drawing[2])
            print(dice_drawing[5])
        case 2, 6:
            print(dice_drawing[2])
            print(dice_drawing[6])
        case 3, 1:
            print(dice_drawing[3])
            print(dice_drawing[1])
        case 3, 2:
            print(dice_drawing[3])
            print(dice_drawing[2])
        case 3, 3:
            print(dice_drawing[3])
            print(dice_drawing[3])
        case 3, 4:
            print(dice_drawing[3])
            print(dice_drawing[4])
        case 3, 5:
            print(dice_drawing[3])
            print(dice_drawing[5])
        case 3, 6:
            print(dice_drawing[3])
            print(dice_drawing[6])
        case 4, 1:
            print(dice_drawing[4])
            print(dice_drawing[1])
        case 4, 2:
            print(dice_drawing[4])
            print(dice_drawing[2])
        case 4, 3:
            print(dice_drawing[4])
            print(dice_drawing[3])
        case 4, 4:
            print(dice_drawing[4])
            print(dice_drawing[4])
        case 4, 5:
            print(dice_drawing[4])
            print(dice_drawing[5])
        case 4, 6:
            print(dice_drawing[4])
            print(dice_drawing[6])
        case 5, 1:
            print(dice_drawing[5])
            print(dice_drawing[1])
        case 5, 2:
            print(dice_drawing[5])
            print(dice_drawing[2])
        case 5, 3:
            print(dice_drawing[5])
            print(dice_drawing[3])
        case 5, 4:
            print(dice_drawing[5])
            print(dice_drawing[4])
        case 5, 5:
            print(dice_drawing[5])
            print(dice_drawing[5])
        case 5, 6:
            print(dice_drawing[5])
            print(dice_drawing[6])
        case 6, 1:
            print(dice_drawing[6])
            print(dice_drawing[1])
        case 6, 2:
            print(dice_drawing[6])
            print(dice_drawing[2])
        case 6, 3:
            print(dice_drawing[6])
            print(dice_drawing[3])
        case 6, 4:
            print(dice_drawing[6])
            print(dice_drawing[4])
        case 6, 5:
            print(dice_drawing[6])
            print(dice_drawing[5])
        case 6, 6:
            print(dice_drawing[6])
            print(dice_drawing[6])

    rolling = input("Roll again? (y/n): ")  
    if rolling.lower() == "y":
        roll()
    else:
        print("Thanks for playing!")
        
if __name__ == '__main__':
    roll()