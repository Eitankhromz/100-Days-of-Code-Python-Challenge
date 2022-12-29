from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Ariel", 40, "italic")
FONT_2 = ("Ariel", 60, "bold")
selected_word = {}

try:
    # USE PANDAS TO READ CSV
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/russian_translation - Sheet1.csv")

    # DATA IS MADE INTO DICT & ORIENTED
    data_dict = original_data.to_dict(orient="records")
else:
    # DATA IS MADE INTO DICT & ORIENTED
    data_dict = data.to_dict(orient="records")

#_________________________________Creating New Flashcards_____________________________________________
def new_card():
    """Selects a new random card and changes the Canvas title and word"""
    global selected_word, flip_timer
    window.after_cancel(flip_timer)
    selected_word = random.choice(data_dict)
    flash_card_canvas.itemconfig(card_title, text="Russian", fill="Black")
    flash_card_canvas.itemconfig(card_word, text=selected_word["Russian"], fill="Black")

    #Change canvas back after revealing answer
    flash_card_canvas.itemconfig(canvas_img, image=front_img)

    #Set equal to variable so canc call window.after_cancel
    flip_timer = window.after(3000, func=flip_card)


#_________________________________Flip Card_____________________________________________
def flip_card():
    """Flips the card and reveals the correct answer"""
    global selected_word
    flash_card_canvas.itemconfig(canvas_img, image=back_img)
    flash_card_canvas.itemconfig(card_title, text="English")
    flash_card_canvas.itemconfig(card_word, text=selected_word["English"], fill="White")

#_________________________________User Knows Card_____________________________________________
def is_known():
    global selected_word
    data_dict.remove(selected_word)
    words_to_learn_data = pd.DataFrame(data_dict)
    words_to_learn_data.to_csv("data/words_to_learn.csv", index=False)

    new_card()

#_________________________________UI_____________________________________________
window = Tk()
window.title("flashY")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)


#CREATE IMAGES INTO USABLE FORMAT
correct_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

#CREATE CANVAS
flash_card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = flash_card_canvas.create_image(400, 263, image=front_img)
#create TITLE
card_title = flash_card_canvas.create_text(400, 150, text="Title (i.e. Language)", font=FONT_1)
#create WORD
card_word = flash_card_canvas.create_text(400, 263, text="Word", font=FONT_2)
flash_card_canvas.grid(column=0, row=0, columnspan=2)

#BUTTONS
green_button = Button(image=correct_img, highlightthickness=0, command=is_known)
green_button.grid(column=1, row=1)

red_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
red_button.grid(column=0, row=1)

#CALL FIRST SO USER DOES NOT SEE DEFAULT
new_card()

window.mainloop()
