from data import racers
import random

class GameLogic:

    def __init__(self, gamemode):
        self.question_number = 0
        self.total_questions = 10
        self.points = 0
        self.racers = racers
        self.current_question = None
        self.gamemode = gamemode

    # Getting the next question from the data
    def next_question(self):
        self.current_question = random.choice(list(self.racers.items()))
        self.question_number += 1
        if self.gamemode == "number":
            return f"Number of {self.current_question[0]}"
        elif self.gamemode == "manufacturer":
            return f"Manufacturer of {self.current_question[0]}"
        else:
            return "Error"

    def check_answer(self, user_answer):
        self.correct_answer = self.current_question[1][self.gamemode]
        if str(user_answer).lower() == str(self.correct_answer).lower():
            self.points += 1
            return True
        else:
            return False
    
    def get_correct_answer(self):
        return f"Correct answer was: {self.correct_answer}"