# Loads questions from json file and convert into python objects

import json
from turtle import title


def load_questions(file_path):

    with open(file_path, 'r') as file:
        questions_data = json.load(file)

    title = questions_data["quiz_title"]
    questions = questions_data["questions"]

    return title, questions
