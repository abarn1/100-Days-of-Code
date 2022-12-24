from tkinter import *
from quiz_brain import QuizBrain
from data import categories_list, get_data
from question_model import *
import random

THEME_COLOR = "#375362"





class QuizStart:

    def __init__(self):

        self.window = Tk()
        self.window.title("Quiz Setup")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.explanation_text = Label(text="Select the options you want to use for the Quiz",
                                      font=('Arial', 12),
                                      bg=THEME_COLOR,
                                      fg='white')
        self.explanation_text.pack(padx = 10, pady = 10, expand = YES, fill = "both")

        self.num_questions = Entry()
        self.num_questions.insert(END, string="20")
        self.num_questions.pack(padx = 10, pady = 10, expand = YES, fill = "both")

        self.categories = Listbox(self.window,
                                  selectmode='multiple')
        for item in categories_list:
            self.categories.insert(END, item)
        self.categories.bind("<<ListboxSelect>>")
        self.categories.select_set(0)
        self.categories.pack(padx = 10, pady = 10, expand = YES, fill = "both")

        self.choice_selection = IntVar()
        self.choice_selection.set(1)
        self.multiple_choice = Radiobutton(text="Multiple Choice", value=1, variable=self.choice_selection,
                                           fg='white',bg=THEME_COLOR)
        self.multiple_choice.pack()
        self.TF_choice = Radiobutton(text="True/False", value=2, variable=self.choice_selection,
                                     fg='white',bg=THEME_COLOR)
        self.TF_choice.pack()

        self.confirm_button = Button(text="Confirm Selection", command=self.get_data, bg=THEME_COLOR)
        self.confirm_button.pack(padx = 10, pady = 10, expand = YES, fill = "both")

        self.data = None
        self.q_type = None

        self.window.mainloop()

    def get_data(self):
        number_of_questions = self.num_questions.get()
        selected_categories = [self.categories.get(cats) for cats in self.categories.curselection()]
        self.q_type = self.choice_selection.get()
        self.data = get_data(self.q_type, int(number_of_questions), selected_categories)

        self.window.destroy()




class TFQuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text='Score: 0', font=('Arial', 12), bg=THEME_COLOR, fg='white', pady=20, padx=20)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background='white')
        self.question = self.canvas.create_text(150,
                                                125,
                                                width=280,
                                                text='Question',
                                                font=('Arial', 20, 'italic'),
                                                fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_img, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_img, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

class MCQuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text='Score: 0', font=('Arial', 12), bg=THEME_COLOR, fg='white', pady=20, padx=20)
        self.score.grid(column=3, row=0)

        self.canvas = Canvas(width=300, height=250, background='white')
        self.question = self.canvas.create_text(150,
                                                125,
                                                width=280,
                                                text='Question',
                                                font=('Arial', 20, 'italic'),
                                                fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=4, pady=50)

        self.button1 = Button(text="Option 1", command=self.b1_pressed)
        self.button1.grid(row=2, column=0)

        self.button2 = Button(text="Option 2", command=self.b2_pressed)
        self.button2.grid(row=2, column=1)

        self.button3 = Button(text="Option 3", command=self.b3_pressed)
        self.button3.grid(row=2, column=2)

        self.button4 = Button(text="Option 4", command=self.b4_pressed)
        self.button4.grid(row=2, column=3)

        self.answer_slot = IntVar()
        self.get_next_question()

        self.window.mainloop()

    def randomization(self, question_options, question_answer):
        question_options.append(question_answer)
        for i in range(0,4):
            selection = random.choice(question_options)
            question_options.remove(selection)
            if i == 0:
                self.button1.config(text=selection)
            elif i == 1:
                self.button2.config(text=selection)
            elif i == 2:
                self.button3.config(text=selection)
            else:
                self.button4.config(text=selection)
            if selection == question_answer:
                self.answer_slot = i
                print(selection)


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            question_text, question_answer, question_options= self.quiz.mc_next_question()
            self.canvas.itemconfig(self.question, text=question_text)
            self.randomization(question_options, question_answer)

        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")
            self.button3.config(state="disabled")
            self.button4.config(state="disabled")


    def b1_pressed(self):
        self.give_feedback(self.quiz.mc_check_answer(self.button1.cget('text')))

    def b2_pressed(self):
        self.give_feedback(self.quiz.mc_check_answer(self.button2.cget('text')))

    def b3_pressed(self):
        self.give_feedback(self.quiz.mc_check_answer(self.button3.cget('text')))

    def b4_pressed(self):
        self.give_feedback(self.quiz.mc_check_answer(self.button4.cget('text')))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)