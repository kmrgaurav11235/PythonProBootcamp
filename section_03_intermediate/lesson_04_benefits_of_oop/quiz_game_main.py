from question_model import Question
from data import question_data

question_bank = []
for data in question_data:
    question = Question(data["text"], data["answer"])
    question_bank.append(question)

for question in question_bank:
    print(f"Q: {question.text}\n A: {question.answer}")