import pandas
from tkinter import *
# from tkinter import messagebox
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("french_words.csv")
french_words = data["French"]
english_words = data["English"]
index = random.randint(0, len(french_words) - 1)


def generate_words():
    
    french_dis = canvas.create_text(400, 263, text=french_words[index], font=("Ariel", 60, "bold"))
    
    
#STEP 1 -LAYOUT 
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file="back.png")
front_image = PhotoImage(file="front.png")
canvas.create_image(400, 263, image=front_image)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text=french_words[index], font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image = wrong_image, highlightthickness=0, command=generate_words)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, highlightthickness=0, command=generate_words)
right_button.grid(column=1, row=1)


#STEP 2 -CREATING NEW FLASH CARDS

















window.mainloop()