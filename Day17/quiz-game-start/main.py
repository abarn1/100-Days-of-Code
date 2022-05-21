# creates the user class(object) from the initial code example representation
class User:
    # this init creates the initial values for the items in the object
    def __init__(self, user_id, username):
        # including a print statement here in the init will print every time the object is created
        # print("new user being created...")
        # initializes the id for the user based on the user_id passed in for the code
        self.id = user_id
        # initializes the username for the user based on the username passed in when the object was created
        self.username = username
        self.followers = 0
        self.following = 0

    # creates a method
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'angela')
user_2 = User('002', 'bob')

user_1.follow(user_2)
print(user_1.following)

# following is the question class usage

from question_model import Question
from data import question_data
from quiz_brain import brain

# creates a list for the question files
q_bank = []
# appends the data from the data file and creates question objects
for question in question_data:
    q_bank.append(Question(question['text'], question['answer']))
# creates the quiz using the quiz_brain class
quiz = brain(q_bank)
# while there are still questions run the quiz checking by using the still_has_questions method
while quiz.still_has_questions():
    # uses the next_question method in the quiz object to move onto the next quiz
    quiz.next_question()
print('You have finished the quiz')
print(f"You ended with a score of {quiz.score}/{quiz.question_number}")

# can I now change the data file to refer to the api at the trivia quiz database
# https://opentdb.com/