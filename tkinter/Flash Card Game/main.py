from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
choice = {}

# ----------------- READ CSV FILE ------------------
try:
    to_learn = pd.read_csv('data/words_to_learn.csv').to_dict(orient='records')
except FileNotFoundError:
    to_learn = pd.read_csv('data/french_words.csv').to_dict(orient='records')


# ----------------- FLIP CARD ------------------
def flip_card():
    canvas.itemconfig(canvas_image, image=card_background)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=choice['English'], fill='white')


# ----------------- NEXT CARD ------------------
def next_card():
    global choice, flip_timer
    window.after_cancel(flip_timer)
    choice = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=choice['French'], fill='black')
    flip_timer = window.after(1000, func=flip_card)


# ----------------- IS KNOWN ------------------
def is_known():
    to_learn.remove(choice)
    pd.DataFrame(to_learn).to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(1000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
card_background = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthicknes=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = Button(image=check_image, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
