import random
from os import system
from art import *
from game_data import data

def clear():
    return system("clear")

def choose_user():
    return random.randint(0, len(data) - 1)

def check_repeated_user(user_a, user_b):
    user_b = choose_user()
    if user_a == user_b:
        check_repeated_user(user_a, user_b)
    else:
        return user_b

def main_game():
    score = 0

    first_user = choose_user()
    second_user = choose_user()
    check_repeated_user(first_user, second_user)

    game_over = False
    while not game_over:
        clear()
        print(logo)
        print(f"Score: {score}")
        print(f"Compare A: {data[first_user]['name']}, a {data[first_user]['description']}, from {data[first_user]['country']}.")
        print(vs)
        print(f"Aganist B: {data[second_user]['name']}, a {data[second_user]['description']}, from {data[second_user]['country']}.")

        choose_a_user = input("Who has more followers? Type 'A' or 'B': ").upper()

        if choose_a_user == 'A':
            player_choice = data[first_user]['follower_count']
            game_choice = data[second_user]['follower_count']
        elif choose_a_user == 'B':
            game_choice = data[first_user]['follower_count']
            player_choice = data[second_user]['follower_count']
        else:
            print("Invalid command, try again")
            input("Press enter to continue...")

        if player_choice > game_choice:
            score += 1
            first_user = second_user
            second_user = choose_user()
            check_repeated_user(first_user, second_user)
        else:
            print("Game Over!")
            replay = input("Do you want to play again? Type 'Y' or 'N': ").upper()
            if replay == "Y":
                main_game()
            elif replay == "N":
                game_over = True
            else:
                print("Invalid command, try again")
                input("Press enter to continue...")

main_game()