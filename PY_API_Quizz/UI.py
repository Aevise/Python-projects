from re import A
from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain
import os

BG_COLOR = "#375362"
BASIC_COLOR = "white"
WRONG_COLOR = "red"
CORRECT_COLOR = "green"
FROM_ROOT = os.path.dirname(os.path.abspath(__file__))
YES_BUTTON = FROM_ROOT + "/images/true.png"
NO_BUTTON = FROM_ROOT + "/images/false.png"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 14, "italic")

class QuizzUI:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.screen = Tk()
        self.screen.title("Quiz Brain")
        self.screen.config(bg = BG_COLOR, padx = 20, pady = 20)
        self.canvas_x = 300
        self.canvas_y = 250

        # ----------------- Images ------------------------
        true_image = PhotoImage(file = YES_BUTTON)
        false_image = PhotoImage(file = NO_BUTTON)

        # ----------------- Label -------------------------
        self.score_label = Label(text = "Score: 0", bg = BG_COLOR, fg = BASIC_COLOR, font = SCORE_FONT)
        self.score_label.grid(row = 0, column = 1)

        # ----------------- Canvas ------------------------
        self.question_canvas = Canvas(width = self.canvas_x, height = self.canvas_y, bg = BASIC_COLOR, highlightthickness = 0)
        self.question_text = self.question_canvas.create_text(self.canvas_x/2, self.canvas_y/2, text = "", fill  = BG_COLOR, font = QUESTION_FONT, width = (self.canvas_x - 20))
        self.question_canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        # ----------------- Buttons -----------------------
        self.false_button = Button(image = false_image, highlightthickness = 0, command = self.false_button_pressed)
        self.false_button.grid(row = 2, column = 0)

        self.true_button = Button(image = true_image, highlightthickness = 0, command = self.true_button_pressed)
        self.true_button.grid(row = 2, column = 1)

        self.next_question()
        self.screen.mainloop()

    # --------------------- Methods -----------------------------------------
    def next_question(self):
        if self.quiz.still_has_question():
            self.question_canvas.config(bg = BASIC_COLOR)
            self.score_label.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question_text()
            self.question_canvas.itemconfig(self.question_text, text = q_text)
        else:
            messagebox.showinfo("End Results", message = f"Congratulations!\nYou have answered {self.quiz.score} questions!")
            self.screen.quit()

    def true_button_pressed(self):
        answer = self.quiz.check_answer("True")
        self.feedback(answer)

    def false_button_pressed(self):
        answer = self.quiz.check_answer("False")
        self.feedback(answer)

    def feedback(self, answer):
        if answer:
            self.question_canvas.config(bg = CORRECT_COLOR)
            self.screen.after(1000, self.next_question)
        else:
            self.question_canvas.config(bg = WRONG_COLOR)
            self.screen.after(1000, self.next_question)


        
