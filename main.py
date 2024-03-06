import random
from art import *
from game_data import data

def choose_user():
    return random.randint(0, len(data) - 1)
    
score = 0

first_user = choose_user()
second_user = choose_user()

game_over = False

print(logo)
print(f"Compare A: {data[first_user]['name']}, a {data[first_user]['description']}, from {data[first_user]['country']}.")
print(vs)
print(f"Aganist B: {data[second_user]['name']}, a {data[second_user]['description']}, from {data[second_user]['country']}.")

user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()