# import random
#
# HARD_MODE=5
# EASY_MODE=10
#
# play_game = True
# while play_game:
#     resume_choice = input("Do you want to play a game of number guessing? Type 'y' or 'n': ")
#     if resume_choice.lower() == "n":
#         play_game = False
#         break
#
#     print("Let's start the game. Hope you have binary search well-understood :)")
#     number_to_guess = random.randrange(1,101)
#     difficulty_level = input("Choose a difficulty level, type \"easy\" or \"hard\": ").lower()
#     game_status = "Lose"
#     if difficulty_level == "easy":
#         num_of_attempts = EASY_MODE
#     elif difficulty_level == "hard":
#         num_of_attempts = HARD_MODE
#     else:
#         print("You didn't choose a listed difficulty level")
#         break
#
#     for attempt in range(num_of_attempts):
#         guess = int(input("Make a guess: "))
#         if guess > number_to_guess:
#             print("too high, try lower")
#         elif guess < number_to_guess:
#             print("too low, try higher")
#         else:
#             print(f"Congrats! You guessed right with -> {guess}")
#             game_status = "Win"
#             break
#
#     if game_status == "Lose":
#         print("You don't have any attempts left :/")

import random
from colorama import Fore, Style, Back


def get_valid_guess():
    """Prompt the user for a valid number guess."""
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print(Back.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)


def set_difficulty():
    """Prompt the user to choose a difficulty level and return the number of attempts."""
    while True:
        difficulty = input("Choose a difficulty level, type \"easy\" or \"hard\": ").lower()
        if difficulty == "easy":
            return EASY_MODE
        elif difficulty == "hard":
            return HARD_MODE
        else:
            print(Fore.YELLOW + "Invalid choice. Please type 'easy' or 'hard'." + Style.RESET_ALL)


def play_number_guessing_game():
    """The main game logic for the number guessing game."""
    print(Fore.GREEN + "Let's start the game. Hope you have binary search well-understood :)" + Style.RESET_ALL)
    number_to_guess = random.randint(1, 101)
    num_of_attempts = set_difficulty()

    for attempt in range(num_of_attempts):
        guess = get_valid_guess()
        if guess > number_to_guess:
            print("Too high. Try lower.")
        elif guess < number_to_guess:
            print("Too low. Try higher.")
        else:
            print(Fore.CYAN + f"Congrats! You guessed right with -> {guess}" + Style.RESET_ALL)
            return
        print(f"Attempt {attempt + 1} of {num_of_attempts}. You have {num_of_attempts - attempt - 1} attempts left.")

    print(
        Fore.RED + f"You've run out of attempts. The number was {number_to_guess}. Better luck next time!" + Style.RESET_ALL)


def main():
    """The main program loop to handle multiple rounds of the game."""
    print(Fore.BLUE + "Welcome to the Number Guessing Game!" + Style.RESET_ALL)
    global HARD_MODE, EASY_MODE
    HARD_MODE = 5
    EASY_MODE = 10

    play_game = True
    while play_game:
        try:
            resume_choice = input("Do you want to play a game of number guessing? Type 'y' or 'n': ").lower()
        except OSError:
            print(Fore.RED + "Error reading input. Exiting the game." + Style.RESET_ALL)
            break

        if resume_choice == 'n':
            play_game = False
            print(Fore.GREEN + "Thanks for playing! See you next time!" + Style.RESET_ALL)
        elif resume_choice == 'y':
            play_number_guessing_game()
        else:
            print(Fore.YELLOW + "Invalid input. Please type 'y' or 'n'." + Style.RESET_ALL)


if __name__ == "__main__":
    try:
        main()
    except OSError:
        print(Fore.RED + "Fatal error: Unable to continue due to input error." + Style.RESET_ALL)

