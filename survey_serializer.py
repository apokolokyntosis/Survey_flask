import json


survey = {}

def create_json():
    survey["pages"] = []
    with open("survey_manual.json", "w") as write_file:
        json.dump(survey, write_file)


def add_question(type,question_text, min, max):
    if type == "rating":
        content = {}
        survey["pages"] .append({
            "name": "",
            "elements": content,
            "type": "type",

            "title": question_text,
            "minRateDescription": min,
            "maxRateDescription": max
        })
    elif type == "boolean":
        survey["pages"].append({
            "type": "pages",
            "name": "",

        })
    elif type == "comment":
