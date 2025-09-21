import random
from tkinter import *
import pandas

#set values
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Calibri", 40, "italic")
WORD_FONT = ("Calibri", 60, "bold")
curr_card, remaining_words_dict = {}, {}

#Card Setup from CSV
try:
    remaining_words_csv = pandas.read_csv("data/remaining_words.csv")
except FileNotFoundError:
    original_df = pandas.read_csv("data/french_words.csv")
    remaining_words_dict = original_df.to_dict(orient="records")
else:
    remaining_words_dict = remaining_words_csv.to_dict(orient="records")

#card generation
def generate_card():
    global curr_card, reset_timer
    #to reset timer when card gets generated (which would happen upon a button click)
    window.after_cancel(reset_timer)
    curr_card = random.choice(remaining_words_dict)

    canvas.itemconfig(card_title, text= "French", fill= "black")
    canvas.itemconfig(card_word, text= curr_card["French"], fill= "black")
    canvas.itemconfig(canvas_image, image= card_front_path)

    reset_timer = window.after(3000, func=flip_card)

# Card Flip Setup
def flip_card():
    canvas.itemconfig(card_title, text= "English", fill= "white")
    canvas.itemconfig(card_word, text= curr_card["English"], fill= "white")
    canvas.itemconfig(canvas_image, image=card_back_path)

# Make the list of words dynamic so that only the remaining words to memorize actually show up
def already_memorized():
    remaining_words_dict.remove(curr_card)
    generate_card()
    remaining_words_df = pandas.DataFrame(remaining_words_dict)
    remaining_words_df.to_csv("data/remaining_words.csv", index= False)

# UI Setup
window = Tk()
window.title("Flashcard Game")
window.config(pady= 50, padx= 50, bg= BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR)
reset_timer = window.after(3000, func=flip_card)

#import images
choice_right_image_path = PhotoImage(file="images/right.png")
choice_wrong_image_path = PhotoImage(file="images/wrong.png")
card_front_path = PhotoImage(file="images/card_front.png")
card_back_path = PhotoImage(file="images/card_back.png")

#set up canvas
canvas = Canvas(width=800, height = 530)
canvas_image = canvas.create_image(400, 260, image=card_front_path)
card_title = canvas.create_text(400, 150, font= TITLE_FONT, fill= "black")
card_word = canvas.create_text(400, 260, font= WORD_FONT, fill="black")
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

#setup buttons
choice_right_button = Button(image=choice_right_image_path, command= already_memorized, highlightbackground=BACKGROUND_COLOR)
choice_wrong_button = Button(image=choice_wrong_image_path, command= generate_card, highlightbackground=BACKGROUND_COLOR)
choice_right_button.grid(row=1, column=1)
choice_wrong_button.grid(row=1, column=0)


# if list is done and all words are memorized
if not remaining_words_dict:
    canvas.itemconfig(card_title, text="Done!", fill="black")
    canvas.itemconfig(card_word, text="🎉", fill="black")

#initiate the first card's generation
generate_card()

window.mainloop()

