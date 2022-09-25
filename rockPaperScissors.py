import random
import sys

def rps():
    options = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice of rock (r), paper (p), or scissors (s).")
    print("Enter 'q' to quit.")
    while True:
        user = input("Enter your choice: ").lower()
        if user == "r" or user == "p" or user == "s":
            user = user.replace("r", "rock").replace("p", "paper").replace("s", "scissors")
        if user == 'q':
            print("Thanks for playing!")
            sys.exit()
        elif user == 'rock' or user == 'paper' or user == 'scissors':
            computer = random.choice(options)
            print("You chose " + user + " and the computer chose " + computer + ".")
            if user == computer:
                print("It's a tie!")
            elif user == 'rock' and computer == 'scissors':
                print("You win!")
            elif user == 'paper' and computer == 'rock':
                print("You win!")
            elif user == 'scissors' and computer == 'paper':
                print("You win!")
            else:
                print("You lose!")
        else:
            print("You did not enter a valid choice.")

if __name__ == '__main__':
    rps()