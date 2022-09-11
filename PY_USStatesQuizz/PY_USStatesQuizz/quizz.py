from turtle import Turtle
import pandas

DATA_PATH = "./50_states.csv"

class StatesQuiz(Turtle):
    def __init__(self):
        super().__init__
        self.correct_answer = []
        self.states = []
        self.states_data = pandas.read_csv(DATA_PATH)
        self.all_states = self.states_data.state.to_list()
        self.number_of_all_states = len(self.all_states)
        self.no_correct_answers = 0
        #self.data_keys = data["state"].to_list

    def is_answer_correct(self, answer:str)->bool:
        """Check whether provided answer matches one of the answers in the data.
        Adds the correct answer to the list.
        """
        if answer in self.all_states and answer not in self.correct_answer:
            self.correct_answer.append(answer)
            return True
        else:
            return False

    def answer(self, answer:str)->None:
        """if the answer is correct calls a function to create a turtle responsible 
        for writing a name of a state on a map. 
        """
        if self.is_answer_correct(answer):
            self.create_inscription(answer)
            self.no_correct_answers = len(self.correct_answer)
            
    def create_inscription(self, answer:str)->None:
        """Creates a new turtle which writes a name of a state on a map
        """
        inscription = Turtle()
        inscription.hideturtle()
        inscription.penup()
        needed_data = self.states_data[self.states_data.state == answer]
        x_cor = int(needed_data["x"])
        y_cor = int(needed_data["y"])
        inscription.goto(x_cor, y_cor)
        inscription.write(answer)
        self.states.append(inscription)

    def continue_game(self)->bool:
        """Returns True when number of correct answers is less than the total amount of states
        """
        if self.no_correct_answers !=  self.number_of_all_states:
            return True
        else:
            return False

    def missed_states(self)->list:
        """Returns a list of states that player didn't typed in
        """
        return list(set(self.all_states) - set(self.correct_answer))