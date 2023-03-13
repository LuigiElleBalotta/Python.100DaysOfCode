from question_model import Question


class QuizBrain:

    def __init__(self, q_list: Question):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        return len(self.question_list) > 0

    def next_question(self):
        current_question = self.question_list.pop(0)
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.get_text()} (True/False): ")
        correct_answer = QuizBrain.check_answer(current_question.get_answer(), user_answer)
        if correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {current_question.get_answer()}.")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print()  # new line
        self.question_number += 1

    @staticmethod
    def check_answer(answer: str, user_answer: str) -> bool:
        return answer.lower() == user_answer.lower()
