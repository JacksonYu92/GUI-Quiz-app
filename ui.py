from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR,fg="white", font=("arial", 15, "bold"))
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="question", fill=THEME_COLOR, font=("arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=30)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, borderwidth=0, bg=THEME_COLOR, command=self.return_true)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, borderwidth=0, bg=THEME_COLOR, command=self.return_false)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def return_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def return_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

