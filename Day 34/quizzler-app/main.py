from question_model import Question
from data import get_data
from quiz_brain import QuizBrain
from ui import QuizInterface

url = "https://opentdb.com/api.php" # api endpoint
# api parameters
params = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

question_data = get_data(url, params=params)

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# ui = MakeGui()
quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
