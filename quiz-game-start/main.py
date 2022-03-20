from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

quiz_questions = []
for i in question_data:
    dict = i
    question = Question(dict["text"], dict["answer"])
    quiz_questions.append(question)

qb = QuizBrain(quiz_questions)

while qb.still_has_questions():
    qb.next_question()

print("You've completed the quiz")f
print(f"Your final score was: {qb.score}/{qb.question_number}")
