from random import randint
from art import *
from game_data import data
from os import system

def clear():
    """Clears the screen"""
    return system("clear")

def choose_user():
    """Returns a user index from data"""
    return randint(0, len(data) - 1)

def check_repeated_user(user_a):
    """Returns the second user"""
    user_b = choose_user()
    if user_a != user_b:
        return user_b
    else:
        check_repeated_user(user_a)

def compare_user_scores(user_a, user_b):
    """Returns the user with greatest score"""
    if data[user_a]['follower_count'] > data[user_b]['follower_count']:
        return 'A'
    else:
        return 'B'

def main_game():
    score = 0
    
    first_user = choose_user()
    second_user = check_repeated_user(first_user)

    game_over = False
    while not game_over:
        clear()
        print(logo)
        print(f"Score: {score}")
        print(f"Compare A: {data[first_user]['name']}, a {data[first_user]['description']}, from {data[first_user]['country']}.")
        print(vs)
        print(f"Aganist B: {data[second_user]['name']}, a {data[second_user]['description']}, from {data[second_user]['country']}.")

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        winner = compare_user_scores(first_user, second_user)

        if choice == winner:
            score += 1
            first_user = second_user
            second_user = check_repeated_user(first_user)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

main_game()