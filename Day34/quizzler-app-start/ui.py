from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text='Score: 0', font=('Arial', 12), bg=THEME_COLOR, fg='white', pady=20, padx=20)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background='white')
        self.question = self.canvas.create_text(150, 125, text='Question', font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_img)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_img)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
