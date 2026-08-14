import pandas as pd
import turtle

#init screen
sc = turtle.Screen()
image_path = "blank_states_img.gif"
sc.title("Game for the US States")
sc.addshape(image_path)
turtle.shape(image_path)

#init data set called state_set and init the list of state names from it
state_set = pd.read_csv("50_states.csv")
state_list = state_set.state.to_list()
num_of_states = len(state_list)
#init the empty list which will take in correct guesses and the missing states
curr_list_of_correct_guess = []
curr_score = len(curr_list_of_correct_guess)
missing_states = []

# def print_states_onto_map(state_name, x_cor, y_cor):
#     turtle.penup()
#     turtle.goto(x_cor, y_cor)
#     turtle.write(state_name)

#core game logic
game_on = True
while curr_score < 50:
    answer_state = sc.textinput(title=f"Guess the States, currently at: {len(curr_list_of_correct_guess)}/{num_of_states}",
                                prompt="Type in a state:").title()

    if answer_state == "Exit":
        game_on = False
        # for state in state_list:
        #     if state not in curr_list_of_correct_guess:
        #         missing_states.append(state)
        #instead of for loop above, use list comprehension
        missing_states = [state for state in state_list if state not in curr_list_of_correct_guess]
        df_missing_states = pd.DataFrame(missing_states)
        df_missing_states.to_csv("states_to_study.csv")

    #check if correct guess
    if answer_state in state_list:
        #init turtle and append to list of correct guesses
        tr = turtle.Turtle()
        tr.hideturtle()
        tr.penup()
        curr_list_of_correct_guess.append(answer_state)

        #go to state's (x,y) and print state name
        state_row_info = state_set[state_set.state == answer_state]
        tr.goto(int(state_row_info.x.item()), int(state_row_info.y.item()))
        tr.write(answer_state) #could use state_row_info.state.item() if needed

