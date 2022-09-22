from cProfile import label
from tkinter import *
from tkinter import messagebox
from dictionary_manager import Word_Dictionary
import pandas

BACKGROUND_COLOR = "#B1DDC6"
TITLE = "Flash Card Learning"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
FRONT_FONT_COLOR = "black"
BACK_FONT_COLOR = "white"
CARD_BACK = "./images/card_back.png"
CARD_FRONT = "./images/card_front.png"
CORRECT_ANSWER_IMAGE = "./images/right.png"
WRONG_ANSWER_IMAGE = "./images/wrong.png"
WORDS_TO_LEARN = "./data/words_to_learn.csv"
WORD = {}
LANGUAGES = []


screen = Tk()
screen.title(TITLE)
screen.config(bg = BACKGROUND_COLOR, padx = 50, pady = 50)
dictionary = Word_Dictionary()
WORD = dictionary.get_word_as_dictionary()
LANGUAGES = list(WORD.keys())
WORD_TO_LEARN = {}

# ---------------------------------methods -----------------------------------------
def new_word()->None:
    """picks a new word from a dictionary and flips a card to the front side
    """
    global WORD, FLIP_TIMER, LANGUAGES
    screen.after_cancel(FLIP_TIMER)
    WORD = dictionary.get_word_as_dictionary()
    card.itemconfig(back_side_language, text = "")
    card.itemconfig(back_side_word, text = "")    
    card.itemconfig(back_side_language_pl, text = "")
    card.itemconfig(back_side_word_pl, text = "")
    card.itemconfig(front_side_language, text = LANGUAGES[0], fill = FRONT_FONT_COLOR)
    card.itemconfig(front_side_language_word, text = WORD[LANGUAGES[0]], fill = FRONT_FONT_COLOR)
    card.itemconfig(card_side, image = front_card_image)
    FLIP_TIMER = screen.after(3000, func = flip_card)

def flip_card()->None:
    """Flips a card to it's back side
    """
    global WORD, LANGUAGES
    card.itemconfig(front_side_language, text = "")
    card.itemconfig(front_side_language_word, text = "")
    card.itemconfig(back_side_language, text = LANGUAGES[1], fill = BACK_FONT_COLOR)
    card.itemconfig(back_side_word, text = WORD[LANGUAGES[1]], fill = BACK_FONT_COLOR)    
    card.itemconfig(back_side_language_pl, text = LANGUAGES[2], fill = BACK_FONT_COLOR)
    card.itemconfig(back_side_word_pl, text = WORD[LANGUAGES[2]], fill = BACK_FONT_COLOR)
    card.itemconfig(card_side, image = back_card_image)

def word_learned()->None:
    """Removes the word from the dictionary and picks a new word
    """
    dictionary.pop_item()
    word_to_learn()
    new_word()

def word_to_learn()->None:
    """Saves the words you need to learn in a new dictionary
    """
    data = pandas.DataFrame(dictionary.word_dictionary)
    data.to_csv(WORDS_TO_LEARN, index = False)

# --------------------- Canvas --------------------------------
front_card_image = PhotoImage(file = CARD_FRONT)
back_card_image = PhotoImage(file = CARD_BACK)
card = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
card_side = card.create_image(400, 263, image = front_card_image)
front_side_language = card.create_text(400, 150,text = LANGUAGES[0] ,font = LANGUAGE_FONT, fill = FRONT_FONT_COLOR)
front_side_language_word = card.create_text(400, 263, text = WORD[LANGUAGES[0]], font = WORD_FONT, fill = FRONT_FONT_COLOR)
back_side_language = card.create_text(400, 50, text = "", font = LANGUAGE_FONT)
back_side_word = card.create_text(400, 163, text = "", font = WORD_FONT)
back_side_language_pl = card.create_text(400, 313, text = "", font = LANGUAGE_FONT)
back_side_word_pl = card.create_text(400, 426, text = "", font = WORD_FONT)
card.grid(row = 0, column = 0, columnspan = 2)

# --------------------- Buttons --------------------------------
ok_image = PhotoImage(file = CORRECT_ANSWER_IMAGE)
ok_button = Button(image = ok_image, highlightthickness=0, command = word_learned)
ok_button.grid(row = 1, column = 1, pady = 25)

wrong_image = PhotoImage(file = WRONG_ANSWER_IMAGE)
wrong_button = Button(image = wrong_image, highlightthickness = 0, command = new_word)
wrong_button.grid(row = 1, column = 0, pady = 25)



FLIP_TIMER = screen.after(3000, func = flip_card)

screen.mainloop()