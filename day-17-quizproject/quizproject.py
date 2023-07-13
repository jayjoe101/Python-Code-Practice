from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['question'], question['answer']))

quiz = QuizBrain(question_bank)

score = 0
while quiz.still_has_questions():
    
    question_num = quiz.question_number + 1
    current_question = quiz.next_question()
    
    user_input = input(f'Q.{question_num}: {current_question.question} (True/False): ')
    
    if user_input == current_question.answer:
        print("Correct!")
        score += 1
    else:
        print (f'You lost, Score: {score}/{question_num}')
        print (f'Correct answer: {current_question.answer}')
        break