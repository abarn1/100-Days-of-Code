from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}


def wrong_answer():
    new_word()


def right_answer():
    global word_dict
    word_dict.remove(word)
    with open('./data/words_to_learn.csv', 'w') as learning:
        pd.DataFrame(word_dict).to_csv('./data/words_to_learn.csv', index=False)
    learning.close()
    word_dict = pd.read_csv('./data/words_to_learn.csv').to_dict(orient='records')
    new_word()


def new_word():
    global answer_timer, word
    window.after_cancel(answer_timer)
    word = random.choice(word_dict)
    lang1, lang2 = word
    flashcard.itemconfig(title_text, text=lang1, fill='black')
    flashcard.itemconfig(word_text, text=word[lang1], fill='black')
    flashcard.itemconfig(card_image, image=front_image)
    answer_timer = window.after(3000, answer_word)


def answer_word():
    global word
    lang1, lang2 = word
    flashcard.itemconfig(title_text, text=lang2, fill='white')
    flashcard.itemconfig(word_text, text=word[lang2], fill='white')
    flashcard.itemconfig(card_image, image=back_image)


try:
    word_dict = pd.read_csv('./data/words_to_learn.csv').to_dict(orient='records')
except FileNotFoundError:
    word_dict = pd.read_csv('./data/french_words.csv').to_dict(orient='records')
    with open('./data/words_to_learn.csv', 'w') as file:
        pd.DataFrame(word_dict).to_csv('./data/words_to_learn.csv', index=False)
    file.close()
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

flashcard = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
front_image = PhotoImage(file='./images/card_front.png')
back_image = PhotoImage(file='./images/card_back.png')
card_image = flashcard.create_image(400, 263, image=front_image)
title_text = flashcard.create_text(400, 150, text="Title", font=('Arial', 40, 'italic'))
word_text = flashcard.create_text(400, 263, text="Word", font=('Arial', 60, 'bold'))
flashcard.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file='./images/wrong.png')
wrong = Button(image=wrong_image, highlightthickness=0, command=wrong_answer)
wrong.grid(row=1, column=0)

right_image = PhotoImage(file='./images/right.png')
right = Button(image=right_image, highlightthickness=0, command=right_answer)
right.grid(row=1, column=1)

answer_timer = window.after(4000, new_word)
new_word()


window.mainloop()
