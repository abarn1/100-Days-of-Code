import json
from math import floor
import requests
from question_model import *
import itertools

parameters = {
    "amount": 20,
    "type": 'multiple',
    "category": 11
}

q_types = {
    "True/False": 'boolean',
    "Multiple Choice": 'multiple'
}
categories_list = ["Film", "Science and Nature", "Sports", "Geography", "Celebrities", "Animals", "Math", "Television",
                   "Gadgets", "Cartoon & Animation"]
categories_dict = {
    "Film": 11,
    "Science and Nature": 17,
    "Sports": 21,
    "Geography": 22,
    "Celebrities": 26,
    "Animals": 27,
    "Math": 19,
    "Television": 14,
    "Gadgets": 30,
    "Cartoon & Animation": 32
}

def get_data(q_type, number, categories):
    per_category = floor(number/len(categories))
    raw_questions = []
    if q_type == 1:
        parameters['type'] = 'multiple'
        for category in categories:
            raw_questions.append(multiple_choice_data(per_category, category))
        list_of_questions = list(itertools.chain.from_iterable(raw_questions))
    else:
        parameters['type'] = 'boolean'
        for category in categories:
            raw_questions.append(true_false_data(per_category, category))
        list_of_questions = list(itertools.chain.from_iterable(raw_questions))
    return list_of_questions
def request_data(number, category):
    parameters['amount'] = number
    parameters['category'] = categories_dict[category]
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    return response.json()['results']
def multiple_choice_data(number, category):
    question_bank = []
    question_data = request_data(number, category)
    for question in question_data:
        question_text = question["question"]
        correct_answer = question["correct_answer"]
        incorrect_answers = question["incorrect_answers"]
        new_question = MCQuestion(question_text, correct_answer, incorrect_answers)
        question_bank.append(new_question)
    return question_bank


def true_false_data(number, category):
    question_bank = []
    question_data = request_data(number, category)
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = TFQuestion(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank

