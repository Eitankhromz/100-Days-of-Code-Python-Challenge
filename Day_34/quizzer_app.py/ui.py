from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT_COLOR = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, background="White")
        self.canvas_text = self.canvas.create_text(150, 125, text="Test Text", font=FONT_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text=f"Score: 0", background=THEME_COLOR, highlightthickness=0, foreground="White")
        self.score.grid(column=1, row=0)

        self.correct_img = PhotoImage(file="images/true.png")
        self.correct = Button(image=self.correct_img, pady=50, highlightthickness=0, command=self.true_pressed)
        self.correct.grid(column=0, row=2)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.wrong_img, pady=20, highlightthickness=0, command=self.false_pressed)
        self.wrong.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.config(bg="White")
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz!")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(background="Red")

        self.window.after(1000, func=self.get_next_question)

