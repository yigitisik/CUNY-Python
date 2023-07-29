from art import logo
from replit import clear
import random

def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level_choice == "easy":
    try_value = 10
  else:
    try_value = 5
  
  number = random.randint(0, 100) # depending on choice 
  
  for _ in range(try_value):
    print(f"You have {try_value} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == number:
      print(f"You got it! The answer was {guess}.")
      break
    elif guess > number:
      print("Too high.")
    else:
      print("Too low.")
    
    try_value -= 1
    if try_value == 0:
      break 
  
  restart = input("Want to play again (yes/no): ")
  if restart == "yes":
    clear()
    play_game()
  else:
    print("Thanks for playing, bye!")


play_game()
