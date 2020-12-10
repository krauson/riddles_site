import requests
from flask import request



def get_riddle():
    # https://opentdb.com/api_config.php
    RIDDLES_API = 'https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple'
    resp = requests.get(RIDDLES_API)
    resp = resp.json()
    print(type(resp))
    quiz_results = resp['results']
    return quiz_results[0]


def get_list_from_str(str_of_list):

    possible_answers = str_of_list[1:-1]

    possible_answers = possible_answers.split(',')

    for i in range(len(possible_answers)):
        possible_answers[i] = possible_answers[i].strip().strip('\'')
    return possible_answers


def format_str(str_param):
    formated = str_param.replace('&quot;', '\"')
    formated = formated.replace('&#039;','\'') 
    formated = formated.replace('&amp;','&') 
    return formated
