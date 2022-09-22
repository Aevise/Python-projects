import pandas
from random import randint
from tkinter import messagebox
import os

DATA_PATH = "./data/dictionary.csv"
WORDS_TO_LEARN = "./data/words_to_learn.csv"

# ---------------------- data extract ------------------------
class Word_Dictionary():
    """Extracts data from the dictionary stored as CSV file.
    """
    def __init__(self) -> None:
        """word_dictionary is a list of dictionaries
        """
        self.word_id = 0
        self.continue_to_learn = True
        self.continue_learning()

    def choose_element(self)->int:
        """Returns:
            int: id of and element from a list of dictionaries
        """
        chosen_id = randint(0, self.words_in_dictionary)
        return chosen_id

    def get_word_as_dictionary(self)->dict:
        """picks word from a list of a dictionary

        Returns:
            dict: containing original word in french and it's translations to languages given in csv file
        """       
        self.word_id = self.choose_element()
        picked_word = self.word_dictionary[self.word_id]    
        return picked_word     

    def get_word_as_list(self)->list:
        """pops a picked word from a list of a dictionary

        Returns:
            list: containing original word in french and it's translations to languages given in csv file
        """
        word_id = self.choose_element()
        picked_word = self.word_dictionary.pop(word_id)
        picked_word_keys = list(picked_word.keys())
        word = [picked_word[key] for key in picked_word_keys]
        self.refresh_data()
        return word

    def get_languages(self)->list:
        """gets a list of languages in csv file

        Returns:
            list: used languages
        """
        languages = list(self.word_dictionary[0].keys())
        return languages

    def refresh_data(self)->None:
        """Refresh data regarding list of dictionaries
        """
        self.words_in_dictionary = len(self.word_dictionary) - 1

    def is_not_empty(self)->None:
        """Check if there is any word left in a list of dictionaries
        """
        if (len(self.word_dictionary) != 0):
            return True
        else:
            return False

    def pop_item(self)->None:
        """Removes and item from the dictionary or list
        """
        self.word_dictionary.pop(self.word_id)
        self.refresh_data()
        
    def continue_learning(self)->None:
        """Pops up a message where you can decide if you want to continue your learning or start anew
        """
        decision = messagebox.askyesno(title = "Continue Learning?", message = "Do you want to continue your learning?")
        if(decision):
            self.continue_to_learn = True
        else:
            self.continue_to_learn = False
        self.create_dictionary()

    def create_dictionary(self)->None:
        """Creates a dictionary of words based on your decision if you want to continue your learning or not
        """
        if self.continue_to_learn:
            try:
                word_dictionary_dataframe = pandas.read_csv(WORDS_TO_LEARN)
            except FileNotFoundError:
                word_dictionary_dataframe = pandas.read_csv(DATA_PATH)
        else:
            os.remove(WORDS_TO_LEARN)
            word_dictionary_dataframe = pandas.read_csv(DATA_PATH)

        self.word_dictionary = word_dictionary_dataframe.to_dict(orient = "records") 
        self.words_in_dictionary = len(self.word_dictionary) - 1
        self.languages = self.get_languages()

