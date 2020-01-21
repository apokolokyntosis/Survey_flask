import json


survey = {}
survey["pages"] = []
question_list = {}

def create_json():
    with open("temp_survey.json", "w") as write_file:
        json.dump(survey, write_file, indent=4)


def add_question(question_type, question_text, min, max):
    if question_type == "rating":
        content = [{
            "type": question_type,
            "name": "question",  # FIXME
            "title": question_text,
            "minRateDescription": min,
            "maxRateDescription": max
        }]
        survey["pages"].append({
            "name": "",
            "elements": content,
        })
        question_list[question_text] =  question_type

    elif question_type == "boolean":
        content = [{
            "type": question_type,
            "name": "question_pie",  # FIXME
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
            "name": "question_cloud",  # FIXME
            "title": question_text,
        }]
        survey["pages"].append({
            "name": "",
            "elements": content
        })
        question_list[question_text] = question_type


def get_questions():
    return question_list



# TODO add progressbar
# showProgressBar: "bottom"

