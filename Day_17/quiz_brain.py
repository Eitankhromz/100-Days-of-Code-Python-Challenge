class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.correct = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ").lower()
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            self.correct+=1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score: {self.correct}/{self.question_number}")
        print()

        if self.question_number == len(self.question_list):
            print("You've completed the the quiz")
            print(f"Your final score was: {self.correct}/{self.question_number}")



