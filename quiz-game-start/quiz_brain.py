class QuizBrain:
    def __init__(self, input_list):
        self.question_number = 0
        self.question_list = input_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        next = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {next.text} (True/False)?: ")
        self.check_answer(answer, next.answer)

    def check_answer(self, user_ans, corr_ans):
        if user_ans.lower() == corr_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {corr_ans}.")
        print(f"Your current score is {self.score}/{self.question_number}")
