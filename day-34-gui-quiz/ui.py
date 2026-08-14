import time
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
GREEN_COLOR = "#759116"
RED_COLOR = "#AA4A44"

class QuizUI:
    def __init__(self, qb: QuizBrain):
        self.quiz = qb

        self.is_user_right = False

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(pady=20, background=THEME_COLOR)

        correct_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=correct_image, highlightthickness=0, command=self.button_correct_check)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.button_false_check)
        self.false_button.grid(row=2, column=1)

        self.score_label = Label(text=f"Score: {self.quiz.score}", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=290, text="Question" , fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=50)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            quiz_content = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_content)

            self.enable_buttons()
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz is finished, see you next time.")

    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def enable_buttons(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")

    def button_correct_check(self):
        is_user_right = self.quiz.check_answer("True")
        self.color_flash_for_answer(is_user_right)

    def button_false_check(self):
        is_user_right = self.quiz.check_answer("False")
        self.color_flash_for_answer(is_user_right)

    def color_flash_for_answer(self, is_user_right):
        self.disable_buttons()
        if is_user_right:
            self.canvas.config(bg=GREEN_COLOR)
        else:
            self.canvas.config(bg=RED_COLOR)
        self.window.after(1000, self.next_question)



