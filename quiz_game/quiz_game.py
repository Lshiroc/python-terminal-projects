import json
import sys

class QuizGame(object):
    score = 0

    def __init__(self, questions):
        self.questionSource = questions

        file = open(questions)
        self.questions = json.load(file)['questions']

    def start(self):
        print("Welcome to the Quiz Game!")
        self.__ready_or_not()
        self.__ask_all()
        self.__result()

    def __ready_or_not(self):
        is_ready = input("Are you ready to go all in? (y/n): ").lower()
        if(is_ready == "n" or is_ready == "no" or is_ready == "nope" or is_ready == "nah"):
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("Oh god! Man up and get on your f**t! You lazy fucker!!")
            print("Getta outta here!")
            print("Log: You got kicked out of the program by the maintainer, haha")
            sys.exit()

        self.score = 0
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("Here we go, do your b*st!")
        print("*************************")

    def __ask_all(self):
        for index, question in enumerate(self.questions):
            self.__ask_single_question(index, question)

    def __ask_single_question(self, i, q):
        answer = input(f"{i+1}. {q['question']}: ")
        self.__validate_answer(answer, q['answer'])

    def __validate_answer(self, user_answ, correct_answ):
        if(user_answ.strip().lower() == correct_answ.strip().lower()):
            print("Correct! Keep going!\n")
            self.score += 1
        else:
            print("Huh? What the hell is this to you, a joke?\n")

    def __result(self):
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print(f"You got {self.score} from {len(self.questions)} questions!")
        print(f"Which is about {(self.score/len(self.questions))*100}% of the quiz.")


newgame = QuizGame("./quiz_questions.json")
newgame.start()
