class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

initial_text = Question("Say", "True")
print(initial_text.text, initial_text.answer)
