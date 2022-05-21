# creates the brain for the quiz
class brain:
    # initializes the variables to use for the object
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # creates the next_question method to get the input from the user, check the results, and move on to the next
    # quiz question
    def next_question(self):
        # gets the data for the current question from the question list
        current_question = self.question_list[self.question_number]
        # gets the input from the user on their answer to the question
        user_answer = input(f'{current_question.text}  (True/False): ')
        # calls the check_answer method to see if the user input was correct
        self.check_answer(user_answer, current_question.answer)
        # increments the question number the quiz is on
        self.question_number += 1

    # method to check if there are any quesions left
    def still_has_questions(self):
        # returns a boolean for if there are any questions left
        return self.question_number < len(self.question_list)

    # check the users answer against the correct answer
    def check_answer(self, user_answer, correct_answer):
        # makes the answers lowercase and checks if they are equivalent
        if user_answer.lower() == correct_answer.lower():
            print('Correct!')
            # increment the users score
            self.score += 1
        else:
            print("That's wrong")
        # print the results of the question and the users score
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number + 1}\n")
