class TFQuestion:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class MCQuestion:
    def __init__(self, q_text, q_answer, q_options):
        self.text = q_text
        self.answer = q_answer
        self.choices = q_options