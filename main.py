from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
if quiz.score >=5:
    print(f"Great Job! Your final score was: {quiz.score}/{quiz.question_number}")
elif quiz.score < 5 and quiz.score >=:
    print(f"You did fine, better luck next time! Your final score was: {quiz.score}/{quiz.question_number}")
else:
    print(f"You failed the test :(, better luck next time! Your final score was: {quiz.score}/{quiz.question_number}")
    
