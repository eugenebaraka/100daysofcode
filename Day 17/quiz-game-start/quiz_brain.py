class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def new_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        prompt = input(f"Q.{self.question_number}: {current_question.question} (True/False)")
        return prompt
