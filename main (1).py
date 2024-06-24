from art import logo, vs
from game_data import data
import random

print(logo)

streak = 0

def random_celeb():
    return random.choice(data)

def compare_celeb(celeb_a, celeb_b):
    if celeb_a['follower_count'] > celeb_b['follower_count']:
        return 'A'
    else:
        return 'B'

# Initial selection of two different celebrities
celeb_1 = random_celeb()
celeb_2 = random_celeb()
while celeb_2 == celeb_1:
    celeb_2 = random_celeb()

choice = ""

while choice != 'Q':
    print(f"Compare A: {celeb_1['name']}, a {celeb_1['description']} from {celeb_1['country']}")
    print(vs)
    print(f"Compare B: {celeb_2['name']}, a {celeb_2['description']} from {celeb_2['country']}")

    choice = input("\nWho has more followers? Type 'A' or 'B' (or 'Q' to quit): ").upper()

    if choice == 'Q':
        print(f"You quit the game. Final streak: {streak}.")
        break

    if choice == compare_celeb(celeb_1, celeb_2):
        streak += 1
        print(f"You're right! Current streak: {streak}.")
        celeb_1 = celeb_2
        celeb_2 = random_celeb()
        while celeb_2 == celeb_1:
            celeb_2 = random_celeb()
    else:
        print(f"Sorry, that's wrong. Final streak: {streak}.")
        break
