from functions import (create_question_list, create_player_list,
                       print_question, print_random_answers, get_player_answer,
                       answer_is_correct, find_winner, display_instructions,
                       answer_is_not_correct)
from json_functions import load_questions
import random
import argparse


def main():
    display_instructions()
    lst_dict_questions = load_questions(args.file_path)
    players = []
    for player in range(args.number_of_players):
        players.append(input("enter name player"))
    list_players_object = create_player_list(players)
    random.shuffle(list_players_object)
    questions = create_question_list(lst_dict_questions)
    random_question = random.choice(questions)
    while len(questions) > 0:
        for player in list_players_object:
            print_question(player, random_question)
            new_mapping = print_random_answers(random_question)
            player_answer = get_player_answer()
            if new_mapping[player_answer] == random_question.correct_answer:
                answer_is_correct(player)
                if len(questions) > 1:
                    questions.remove(random_question)
                    random_question = random.choice(questions)
                else:
                    questions.pop(0)
                    break
            else:
                answer_is_not_correct(player)

    winner = find_winner(list_players_object)
    print(f"You win Mr. {winner.name} you got {winner.score} points")


# main()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trivia Game CLI")
    parser.add_argument("--file_path", type=str, required=True, help="file path")
    parser.add_argument("--number_of_players", type=int, required=True, help="numbers of players")
    args = parser.parse_args()
    main()
