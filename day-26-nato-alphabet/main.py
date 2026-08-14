import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import turtle
#init screen
sc = turtle.Screen()
sc.title("Nato Letter Game")
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
nato_letter_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (letter, row) in nato_letter_df.iterrows()}
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
game_on = True
while game_on:
    try:
        user_input = sc.textinput("Type a word to letter out in nato scheme: ", "Type word: ").upper()
        if user_input == "EXIT":
            game_on = False
            print("Game is turned off.")
            break
        nato_coded_letters = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Please type in letters only.")
    else:
        print(nato_coded_letters)


