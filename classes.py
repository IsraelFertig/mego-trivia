class A_Question:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
