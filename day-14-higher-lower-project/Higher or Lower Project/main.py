from art import logo, vs
from game_data import game_data
import random


def higherLower(A, B):
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.\n" + vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}.")

    if A['follower_count'] > B['follower_count']:
        winner = "A"
        loser = "B"
    elif A['follower_count'] < B['follower_count']:
        winner = "B"
        loser = "A"
    else:
        winner = "DRAW"
        loser = None  # In case of a draw, no one is removed

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    return guess == winner, winner, loser


def play():
    game_data_copy = game_data.copy()  # Work with a copy to avoid modifying the original list
    A = random.choice(game_data_copy)
    score = 0

    while True:
        print(logo)
        dataWithARemoved = [entry for entry in game_data_copy if entry != A]

        if not dataWithARemoved:  # No more comparisons possible
            print(f"Congratulations! You guessed all correctly. Final score: {score}")
            break

        B = random.choice(dataWithARemoved)
        isUserCorrect, winner, loser = higherLower(A, B)

        if not isUserCorrect:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break

        score += 1
        if loser in game_data_copy:
                game_data_copy.remove(next(entry for entry in game_data_copy if entry == loser))  # Safe removal
        print(f"You're right! Current score: {score}")

        if winner == "B":  # Carry forward B as the new A
            A = B

play()
