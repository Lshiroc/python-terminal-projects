import random
import sys
import math
import time

class NumberGuesser(object):
    def __init__(self, range, startrange=1):
        self.range = range
        self.startrange = startrange
        self.guesses = 0
        print("Welcome to Number Guesser Game!")
        

    def is_ready(self):
        answers = ["y", "yeah", "yes", "yep", "yup", "yeas"]
        answer = input("Are you ready to start? <y/n>: ").lower()
        if answer in answers:
            print("Okay!    Here we go young buck! Hold on tight!\n")
            return True
        else:
            print("Sad to hear that, come back soon!")
            sys.exit()
    
    def new_number(self):
        self.num = random.randint(self.startrange, self.range)

    def player_try(self):
        self.guesses += 1
        guess = int(input("Your guess: "))
        
        if guess == self.num:
            print("You guessed it correctly!")
            print(f"Guesses: {self.guesses}")
            print(f"You have successfully wasted {math.ceil(time.time() - self.wastedtimestart)} seconds of your life!")
            return True
        else:
            print('WRONG! pathetic..., Try again!\n')
            return False

    def start(self):
        if self.is_ready():
            self.wastedtimestart = time.time()
            self.new_number()
            print(f"Which Number I have in mind between {self.startrange} and {self.range}? ")
            while(True):
                result = self.player_try()
                if result:
                    sys.exit()

newgame = NumberGuesser(15, 1)
newgame.start()
