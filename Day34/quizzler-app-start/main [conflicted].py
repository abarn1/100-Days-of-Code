from quiz_brain import QuizBrain
from ui import TFQuizInterface, QuizStart, MCQuizInterface


quiz_selection = QuizStart()
quiz = QuizBrain(quiz_selection.data)
if quiz_selection.q_type == 1:
    quiz_ui = MCQuizInterface(quiz)
else:
    quiz_ui = TFQuizInterface(quiz)

