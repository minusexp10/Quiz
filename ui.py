import tkinter
from tkinter import *
from quiz_brain import QuizBrain
from data import data
from question_model import Question

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizium")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0, bg='pink')
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text='question',
            justify='center',
            fill=THEME_COLOR,
            font=('Ariel', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file='./images/true.png')
        self.tick = Button(image=true_img, command=self.tick_fn)
        self.tick.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0)
        self.tick.grid(column=1, row=2)

        false_img = PhotoImage(file='./images/false.png')
        self.cross = Button(image=false_img, command=self.cross_fn)
        self.cross.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0)
        self.cross.grid(column=0, row=2)

        self.score = Label(text='Score: 0', font=('Courier', 12, 'bold'), bg=THEME_COLOR)
        self.score.config(fg='white', padx=20, pady=20)
        self.score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text='You have reached the end of the quiz')
            self.tick.config(state='disabled')
            self.cross.config(state='disabled')

    def tick_fn(self):
        if self.quiz.check_answer('True'):
            self.canvas.config(bg='Green')
            self.canvas.itemconfig(self.question, fill='white')
        else:
            self.canvas.config(bg='Red')
            self.canvas.itemconfig(self.question, fill='white')
        self.score.config(text=f'Score: {self.quiz.score}')
        self.window.after(1000, self.get_next_question)


    def cross_fn(self):
        if self.quiz.check_answer('False'):
            self.canvas.config(bg='Green')
            self.canvas.itemconfig(self.question, fill='white')
        else:
            self.canvas.config(bg='Red')
            self.canvas.itemconfig(self.question, fill='white')
        self.score.config(text=f'Score: {self.quiz.score}')
        self.window.after(1000, self.get_next_question)
