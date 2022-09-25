from UI import QuizzUI
from question_model import Question
from data import database
from quiz_brain import QuizBrain

question_bank = []

for question in database:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    question_bank.append(Question(q_text, q_answer))

quiz = QuizBrain(question_bank)
quiz_ui = QuizzUI(quiz)

print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")