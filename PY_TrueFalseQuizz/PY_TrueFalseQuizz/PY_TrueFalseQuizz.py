from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

data_keys = list(question_data[0].keys())
question_bank = []

for question in question_data:
   q_text = question[data_keys[0]]
   q_answer = question[data_keys[1]]
   question_bank.append(Question(q_text, q_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
   quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")