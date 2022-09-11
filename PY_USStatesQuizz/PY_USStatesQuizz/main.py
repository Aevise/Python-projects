import pandas
import turtle
from quizz import StatesQuiz

TITLE = "U.S. States Game"
IMAGE_PATH = "./blank_states_img.gif"
MISSED_STATES = "./missed_states.csv"
RESOLUTION = (500, 725)

def screen_setup():
    screen.title(TITLE)
    screen.addshape(IMAGE_PATH)
    screen.setup(height = RESOLUTION[0], width = RESOLUTION[1])
    turtle.shape(IMAGE_PATH)


screen = turtle.Screen()
screen_setup()
quiz = StatesQuiz()
is_game_on = True

while is_game_on:
    my_answer = screen.textinput(title = "Guess the State", 
    prompt = f"{quiz.no_correct_answers}/{quiz.number_of_all_states} States Correct").title()
    if my_answer == "Exit":
        break
    quiz.answer(my_answer)
    is_game_on = quiz.continue_game()

missed_answers = pandas.Series(quiz.missed_states()) 
missed_answers.to_csv(MISSED_STATES)

#getting coordinates from a map
#def get_mouse_click_cor(x,y):
#    print(x,y)
#turtle.onscreenclick(get_mouse_click_cor)

turtle.mainloop()

