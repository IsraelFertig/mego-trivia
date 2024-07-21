from classes import A_Question, Player
import random


def create_trivia_question(question):
    question_object = A_Question(question["question"],
                                 question["answers"],
                                 question["correct_answer"])
    return question_object


def create_question_list(lst_dict_questions):
    list_objects_questions = []
    for question in lst_dict_questions:
        list_objects_questions.append(create_trivia_question(question))
    return list_objects_questions


def create_player_list(list_players_name):
    players_list = []
    for player_name in list_players_name:
        players_list.append(Player(player_name))
    return players_list


def print_question(player, question):
    print(f"Hello {player.name}")
    print(f"your question is: {question.question}")


def print_random_answers(question):
    answers_list = list(question.answers.values())
    random.shuffle(answers_list)
    # Create a new mapping
    new_mapping = {str(i): key for i, (key) in enumerate(answers_list, 1)}
    # The answers are printed in random order, but with ordered numbers
    for i, (value) in enumerate(answers_list, 1):
        print(f"{i}. {value}")
    return new_mapping


def get_player_answer():
    return input("Please enter your answer")


def answer_is_correct(player):
    print(f"Very Good, correct answer Mr, {player.name}")
    player.score += 1


def answer_is_not_correct(player):
    print(f"I'm sorry Mr {player.name}, wrong answer")


def find_winner(players):
    return max(players, key=lambda player: player.score)


def display_instructions():
    print("""
Game Instructions:
1. The game presents trivia questions to each player in turn.
2. Answer the question by choosing the number corresponding to the answer.
3. A correct answer earns a point and the player continues to the next question.
4. The game continues until all questions have been asked.
5. The player with the highest score wins.
""")
