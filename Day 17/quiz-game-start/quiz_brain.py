class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.points = 0

    def still_has_question(self):
        n_questions = len(self.question_list)
        if n_questions >= self.question_number + 1:
            return True
        else:
            print(f"You've completed the quiz! Your final score is {self.points}/{n_questions}")


    def new_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.points += 1
            print(f"Your current score is: {self.points}/{self.question_number}")
        else:
            print(f"Your current score is: {self.points}/{self.question_number}")
        print(f"Correct answer: {correct_answer}\n")




