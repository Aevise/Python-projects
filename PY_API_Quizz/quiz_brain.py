import html

class QuizBrain():
    def __init__(self, q_list: list) -> None:
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def next_question_text(self)->str:
        self.current_question = self.questions_list[self.question_number]
        self.question_number += 1
        formatted_question = html.unescape(self.current_question.text)       #unescapes html format

        return f"Q.{self.question_number}: {formatted_question}?"

    def still_has_question(self)->bool:
        """
        Check if there are another questions in question pool
        """
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer:str)->bool:
        """
        Check whether answer is correct and print output information.
        Increment score of player each time he guess right.
        """
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False