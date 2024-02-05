import random
import sys

class Game(object):
    def __init__(self):
        print("Welcome to Rock Paper Scissors Game!")

    def is_ready(self):
        answer = input("Are you ready to begin? <y/n>: ")
        answers = ["y", "yeah", "yes", "yep", "yup"]

        if answer in answers:
            print("Okayyy, Here we go!")
        else:
            print("What a coward!")
            sys.exit()

    def counter_response(self):
        moves = ['rock', 'paper', 'scissors']
        self.response = moves[random.randint(0, 2)]

    def user_response(self):
        self.move = input("What's your move: ").lower()
        print(f"\n{self.move} X {self.response}")
        if (self.move == "rock" and self.response == "paper") or (self.move == "paper" and self.response == "scissors") or (self.move == "scissors" and self.response == "rock"):
            print("LMAO! what a loser!")
        elif (self.move == "rock" and self.response == "rock") or (self.move == "paper" and self.response == "paper") or (self.move == "scissors" and self.response == "scissors"):
            print("Pfft, lucky move, it's a tie.")
        elif (self.move == "rock" and self.response == "scissors") or (self.move == "paper" and self.response == "rock") or (self.move == "scissors" and self.response == "paper"):
            print("Luck is on your side, huh. Okay okay, YOU WON!")

        sys.exit()
    def start(self):
        self.is_ready()
        self.counter_response()
        self.user_response()



newgame = Game()
newgame.start()