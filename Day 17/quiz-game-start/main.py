from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question_answer_ in question_data:
    question = question_answer_["question"]
    answer = question_answer_["correct_answer"]
    new_question = Question(question=question, answer=answer)

    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.new_question()





