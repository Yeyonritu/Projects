import pandas
from tkinter import *
# from tkinter import messagebox
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
    
except FileNotFoundError:
    original_path = pandas.read_csv("french_words.csv")
    to_learn = original_path.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    
    
def generate_words():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(french_dis, text=current_card["French"], fill = "black")
    canvas.itemconfig(initial_image, image=front_image)
    window.after(3000, flip_card)
    
def flip_card():
    
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(french_dis, text=current_card["English"], fill="white")
    canvas.itemconfig(initial_image, image=back_image)
    
def already_learnt():
    
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    
    generate_words()
    
    
#STEP 1 -LAYOUT 
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file="back.png")
front_image = PhotoImage(file="front.png")
initial_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
french_dis = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image = wrong_image, highlightthickness=0, command=generate_words)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, highlightthickness=0, command =already_learnt)
right_button.grid(column=1, row=1)

window.mainloop()