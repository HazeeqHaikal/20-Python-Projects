import random
import sys

def rps():
    options = ["rock", "paper", "scissors"]
    userPoints = 0
    computerPoints = 0
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice of rock (r), paper (p), or scissors (s).")
    print("Enter 'q' to quit.")
    while True:
        user = input("Enter your choice: ").lower()
        if user == "r" or user == "p" or user == "s":
            user = user.replace("r", "rock").replace("p", "paper").replace("s", "scissors")
        if user == 'q':
            print("")
            if userPoints > computerPoints:
                print("You won!")
            elif userPoints < computerPoints:
                print("Computer won!")
            else:
                print("You and computer got a tie!")
            print("Thanks for playing! Your last score is {} and computer is {}.".format(userPoints, computerPoints))
            sys.exit()
        elif user == 'rock' or user == 'paper' or user == 'scissors':
            computer = random.choice(options)
            print("You chose " + user + " and the computer chose " + computer + ".")
            if user == computer:
                print("It's a tie!")
            elif user == 'rock' and computer == 'scissors':
                print("You win!")
                userPoints += 1
            elif user == 'paper' and computer == 'rock':
                print("You win!")
                userPoints += 1
            elif user == 'scissors' and computer == 'paper':
                print("You win!")
                userPoints += 1
            else:
                print("You lose!")
                computerPoints += 1
        else:
            print("You did not enter a valid choice.")

if __name__ == '__main__':
    rps()