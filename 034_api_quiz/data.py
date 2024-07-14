import requests
from question_model import Question

params = {
    'amount': 10,
    'type': 'boolean'
}

def fetch_questions():
    response = requests.get("https://opentdb.com/api.php", params=params)
    questions = response.json().get('results', [])
    question_list = [{'question': q['question'], 'correct_answer': q['correct_answer']} for q in questions]
    question_bank = [Question(question["question"], question["correct_answer"]) for question in question_list]
    return question_bank

question_bank = fetch_questions()