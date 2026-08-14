from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz_content = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz_content)

# commenting this out given that ui.py checks mainloop()
# while quiz.still_has_questions():
#     quiz.next_question()
