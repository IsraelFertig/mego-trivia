from functions import *
from json_functions import *


def main():
    lst = load_questions("trivia_questions.json")
    num_of_players = int(input("Please enter the number of players"))
    players = []
    for player in range(num_of_players):
        players.append(input("enter name player"))
    players = createPlayerList(players)
    questions = (createQuestionList(lst))
    random_item = random.choice(questions)
    current_player = 0
    while questions:
        for player in players:
            print_question(player, random_item)
            new_mapping = print_random_answers(random_item)
            player_answer = get_player_answer()
            if new_mapping[player_answer] == random_item.correct_answer:
                handle_correct_answer(player, questions, random_item)
                if len(questions) > 1:
                    questions.remove(random_item)
                    random_item = random.choice(questions)
                else:
                    questions.pop(0)
                    break
    winner = find_winner(players)
    print(f"You win Mr. {winner.name} you got {winner.score} points")


main()
