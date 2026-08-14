from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "A"
  else:
    return guess == "B"
    
def play_game():
  print(logo)
  score = 0
  game_not_over = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_not_over == True:
    #when guess is right, b gets switched to a and new account gets to b
    account_a = account_b
    account_b = get_random_account()
    while account_a == account_b:
      account_b = get_random_account()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ")
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")    
    else:
      print(f"Sorry that's wrong. Final score is {score}")
      game_not_over = False

want_to_play = True
while want_to_play == True:
  choice = input("Click and type 'Y' to start, 'N' to quit: " )
  if choice == "Y":
    clear()
    play_game()
  else:
    clear()
    print("Bye, thanks for stopping by!")
    want_to_play = False
                 