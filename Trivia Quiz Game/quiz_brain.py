class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, player_choice,  correct_answer):
        if player_choice.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You had it wrong :/")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_choice = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(player_choice, current_question.answer)
