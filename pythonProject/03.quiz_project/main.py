from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)

quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_questions():
    quizBrain.next_question()

print(f"You've completed the quiz! Your score is: {quizBrain.score}")
