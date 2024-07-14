from classes import *
import random


def createTriviaQuestion(question):
    question_object = A_Question(question["question"],
                                 question["answers"],
                                 question["correct_answer"])
    return question_object


def createQuestionList(lst):
    questions = []
    for question in lst:
        questions.append(createTriviaQuestion(question))
    return questions


def createPlayer(name):
    a = Player(name)
    return a


def createPlayerList(listPlayersName):
    playersList = []
    for player in listPlayersName:
        playersList.append(createPlayer(player))
    return playersList


def print_question(player, question):
    print(f"Hello {player.name}")
    print(f"your question is: {question.question}")


def print_random_answers(question):
    answers_list = list(question.answers.values())
    random.shuffle(answers_list)
    # מדפיסים את התשובות בסדר אקראי, אבל עם מספרים מסודרים
    for i, (value) in enumerate(answers_list, 1):
        print(f"{i}. {value}")
    #
    # # יוצרים מיפוי חדש
    new_mapping = {str(i): key for i, (key) in enumerate(answers_list, 1)}
    return new_mapping


def get_player_answer():
    return input("Please enter your answer")


def handle_correct_answer(player, questions, random_item):
    print(f"Very Good, correct answer Mr, {player.name}")
    player.score += 1


def find_winner(players):
    return max(players, key=lambda player: player.score)
