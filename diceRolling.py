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
    print("\n".join([dice_drawing[dice1], dice_drawing[dice2]]))
    

    rolling = input("Roll again? (y/n): ")  
    if rolling.lower() == "y":
        roll()
    else:
        print("Thanks for playing!")
        
if __name__ == '__main__':
    roll()