import json
import html
import requests


class QuizSetup:
    def __init__(self, player: str, amount: int, difficulty: str, type: str, category: int):
        self.all_answers_temp = None
        self.player = player
        self.amount = amount
        self.difficulty = difficulty
        self.type = type
        self.category = category
        self.question_api = "https://opentdb.com/api.php"
        self.correct_answer = None
        self.all_answers = None
        self.question = None
        self.total_questions = None
        self.quiz_list = None
        self.question_number = 1
        self.question_index = 0
        self.score = 0
        self.create_quiz_data()

    def create_quiz_data(self):
        quiz_parameters = {
            'amount': self.amount,
            'difficulty': self.difficulty,
            'type': self.type,
            'category': self.category
        }
        quiz_request = requests.get(self.question_api, params=quiz_parameters)
        quiz_request.raise_for_status()
        with open("data/question_temp.json", 'w') as quiz_file:
            json.dump(quiz_request.json(), quiz_file, indent=4)

        with open("data/question_temp.json", 'r') as quiz_file:
            quiz_data = json.load(quiz_file)
        return quiz_data

    def start_quiz(self):
        self.quiz_list = self.create_quiz_data()['results']
        self.total_questions = len(self.quiz_list)
        if self.type == 'multiple':
            self.multiple_quiz()
        else:
            self.boolean_quiz()

    def multiple_quiz(self):
        self.question = html.unescape(self.quiz_list[self.question_index]['question'])
        self.all_answers_temp = self.quiz_list[self.question_index]['incorrect_answers']
        self.all_answers_temp.append(
            self.quiz_list[self.question_index]['correct_answer'])
        self.all_answers = [html.unescape(i) for i in self.all_answers_temp]
        self.correct_answer = html.unescape(self.quiz_list[self.question_index]['correct_answer'])
        self.all_answers_temp = []

    def boolean_quiz(self):
        self.question = html.unescape(self.quiz_list[self.question_index]['question'])
        self.correct_answer = html.unescape(self.quiz_list[self.question_index]['correct_answer'])

    def next_question(self):
        self.question_index += 1
        self.question_number += 1
        if self.type == 'multiple':
            self.multiple_quiz()
        else:
            self.boolean_quiz()

    def check_answers(self, answer):
        if answer == self.correct_answer:
            return True
        else:
            return False

    def is_finish(self):
        if self.total_questions > self.question_index + 1:
            return True
        else:
            return False

