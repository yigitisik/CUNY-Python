import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
    print(rock + "lost")
  elif computer_choice == 1:
    print(paper + "win!")
  else:
    print(scissors + "draw")
else:
  print("Invalid argument.")

# OTHER COMMON METHOD FOR KIDS TO GRASPY EASILY FOR THE LOGICAL IF S
#
# if player_choice == 0:
#   print(rock)
#   if computer_choice == 0:
#     print(rock + "draw")
#   elif computer_choice == 1:
#     print(paper + "lost")
#   else:
#     print(scissors + "win!")
# elif player_choice == 1:
#   print(paper)
#   if computer_choice == 0:
#     print(rock + "win!")
#   elif computer_choice == 1:
#     print(paper + "draw")
#   else:
#     print(scissors + "lost")
# elif player_choice == 2:
#   print(scissors)
#   if computer_choice == 0:
#     print(rock + "lost")
#   elif computer_choice == 1:
#     print(paper + "win!")
#   else:
#     print(scissors + "draw")
# else:
#   print("Invalid argument.")