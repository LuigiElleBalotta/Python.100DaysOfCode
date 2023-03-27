from tkinter import *
from tkinter import messagebox
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA INITIALIZATION ------------------------------- #
try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    messagebox.showerror(title="File not found", message="The file 'french_words.csv' was not found.")
    exit()
else:
    print(data)

to_learn = data.to_dict(orient="records")
print(to_learn)

# Override the to_learn list with the words_to_learn.csv file if it exists
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    pass
else:
    to_learn = data.to_dict(orient="records")


flip_card_timer = None
current_card = None


def update_title_and_word():
    global to_learn
    global flip_card_timer
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_label, text="French", fill="black")
    canvas.itemconfig(world_label, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_card_timer = canvas.after(3000, flip_card, current_card)


def save_unknown_word_to_csv_file():
    global to_learn
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)


def move_word_to_bottom_of_list():
    global to_learn, current_card
    to_learn.append(current_card)
    to_learn.remove(current_card)
    current_card = None


def remove_word_from_list():
    global to_learn, current_card
    to_learn.remove(current_card)
    current_card = None


def unknown_button_clicked():
    global flip_card_timer
    canvas.after_cancel(flip_card_timer)
    move_word_to_bottom_of_list()
    save_unknown_word_to_csv_file()
    update_title_and_word()


def known_button_clicked():
    global flip_card_timer
    canvas.after_cancel(flip_card_timer)
    remove_word_from_list()
    save_unknown_word_to_csv_file()
    update_title_and_word()


def flip_card(*args):
    canvas.itemconfig(title_label, text="English", fill="white")
    canvas.itemconfig(world_label, text=args[0]["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back_img)


# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas.grid(row=0, column=0, columnspan=2)
card_image = canvas.create_image(400, 263, image=card_front_img)

# Title label
title_label = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))

# Word label
world_label = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


# Wrong Button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, bd=0, command=unknown_button_clicked)
unknown_button.grid(row=1, column=0)

# Right Button
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, bd=0, command=known_button_clicked)
known_button.grid(row=1, column=1)

update_title_and_word()

window.mainloop()
