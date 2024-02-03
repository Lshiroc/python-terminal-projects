import random
import sys

class NumberGuesser(object):
    def __init__(self, range, start=1):
        self.range = range
        self.start = start
        print("Welcome to Number Guesser Game!")
        if self.is_ready():
            self.new_number()
            print(f"Which Number I have in mind between {self.start} and {self.range}? ")
            self.start()

    def is_ready(self):
        answers = ["yeah", "yes", "yep", "yup", "yeas"]
        answer = input("Are you ready to start? <y/n>: ").lower()
        if answer in answers:
            print("Okay! Here we go young buck! Hold on tight!\n")
            return True
        else:
            print("Sad to hear that, come back soon!")
            sys.exit()
    
    def new_number(self):
        self.num = random.randint(self.start, self.range)

    # def player_try(self):
    # def start(self):

newgame = NumberGuesser(15, 1)


