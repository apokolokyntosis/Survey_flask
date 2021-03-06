import json
import random
from flask import session


# FIXME ?
survey = {}
survey["pages"] = []
question_list = {}


# creates a json from the dict
# FIXME write json to program folder
def create_json():
    survey["showProgressBar"] = "bottom"
    with open("temp_survey.json", "w") as write_file:
        json.dump(survey, write_file, indent=4)


# adds question to the survey dict
def add_question(question_type, question_text, choices=None):
    if question_type == "rating":
        content = [{
            "type": question_type,
            "name": "question{}".format(random.randint(0, 10000)),
            "title": question_text,
            "minRateDescription": 0,
            "maxRateDescription": 5
        }]
        survey["pages"].append({
            "name": "",
            "elements": content,
        })
        question_list[question_text] = question_type

    elif question_type == "boolean":
        content = [{
            "type": question_type,
            "name": "question{}pie".format(random.randint(0, 10000)),
            "title": question_text,
            "indent": 5,
            "isRequired": "true",
            "labelTrue": "Ja",
            "labelFalse": "Nein"
        }]
        survey["pages"].append({
            "name": "",
            "elements": content
        })
        question_list[question_text] = question_type

    elif question_type == "comment":
        content = [{
            "type": question_type,
            "name": "question{}cloud".format(random.randint(0, 10000)),
            "title": question_text,
        }]
        survey["pages"].append({
            "name": "",
            "elements": content
        })
        question_list[question_text] = question_type

    elif question_type == "text":
        content = [{
            "type": question_type,
            "name": "question{}cloud".format(random.randint(0, 10000)),
            "title": question_text,
        }]
        survey["pages"].append({
            "name": "",
            "elements": content
        })
        question_list[question_text] = question_type

    elif question_type == "radiogroup":
        content = [{
            "type": question_type,
            "name": "question{}pie".format(random.randint(0, 10000)),
            "title": question_text,
            "choices": choices
        }]
        survey["pages"].append({
            "name": "",
            "elements": content
        })
        question_list[question_text] = question_type


# Getter for list of questions shown during the creation process
def get_questions():
    return question_list


def clear_memory():
    survey.clear()
    survey["pages"] = []
    question_list.clear()

# TODO add progressbar
# showProgressBar: "bottom"

