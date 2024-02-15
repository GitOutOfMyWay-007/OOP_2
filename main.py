from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # We are creating a question bank(this empty list) which is a list of question objects
for question in question_data:
    question_text = question["question"]  # text is key of the questions in question_data
    question_answer = question["correct_answer"]  # answer is key of the answers in question_data
    new_question = Question(text=question_text, answer=question_answer)  # Creating new_ques(OBJECT)
    # from the Question Class (in question_model file (the text and answer are parameters of the Question class)
    # Whenever an OBJECT of Question class is created (here new_ques being created)
    # values for "text" and "answer" are passed as arguments to the Class
    question_bank.append(new_question)  # filling the new_ques(object) into the empty list (so we can work in main.py)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations! You have completed the Quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")



#print(question_bank)  # will print the memory locations question items in the list
