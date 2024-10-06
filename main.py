import tkinter

from question_model import Question
from data import data
from quiz_brain import QuizBrain
from ui import QuizInterface
from tkinter import *

type_selection = Tk()
type_selection.title("Selection")
type_selection.config(bg="#375362", padx=50, pady=50)

heading = Label(text='Select the type of quiz you want to give', font=('Ariel', 20, 'italic'))
heading.config(fg='white', bg="#375362", padx=20, pady=20)
heading.grid(column=0, row=0)

option = [
        'General Knowledge',
        'Science: Computers',
        'Entertainment: Cartoon & Animations',
        'Entertainment: Video Games',
        'Entertainment: Japanese Anime and Manga',
        'Mythology',
        'Politics'
]

clicked = tkinter.StringVar()
clicked.set('General Knowledge')
drop = tkinter.OptionMenu(type_selection, clicked, *option)
drop.config(highlightthickness=0, padx=5, pady=5)
drop.grid(column=0, row=1)

continue_button = Button(text='Continue..', command=type_selection.destroy)
continue_button.grid(column=0, row=2, pady=20)
type_selection.mainloop()

# print(clicked.get())
quiz_type = clicked.get()
questions = data(quiz_type)
question_bank = []
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
