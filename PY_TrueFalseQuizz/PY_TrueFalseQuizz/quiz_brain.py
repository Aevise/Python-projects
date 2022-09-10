class QuizBrain():
    def __init__(self, q_list: list) -> None:
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        check_condition = True
        while check_condition:
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").capitalize()
            if(user_answer == "True" or user_answer == "False"):
                check_condition = False
        self.check_answer(user_answer, current_question.correct_answer)

    def still_has_question(self)->bool:
        """
        Check if there are another questions in question pool
        """
        return self.question_number < len(self.questions_list)
        #try:
        #    self.questions_list[self.question_number]
        #    return True
        #except IndexError:
        #    return False

    def check_answer(self, user_answer:str, correct_answer:str)->None:
        """
        Check whether answer is correct and print output information.
        Increment score of player each time he guess right.
        """
        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("Sorry, that's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")