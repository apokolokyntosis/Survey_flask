import requests

accesskey = "3bc43120cf784d489aefbc4cec9b1268"


def get_questions(uid):
    dict = get_titles(uid)
    questions = []
    for key in dict:
        questions.append(str(key))
    return questions


# parses results for a specific question into a list
def get_results_for_question(s_results, question):
    q_results = []
    for entry in s_results["Data"]:
        if "{}".format(question) in entry.keys():
            q_results.append(str(entry[question]))
    return q_results


# creates a dict consisting of q_name : q_title
def get_titles(uid):
    s_data = load_survey(uid)
    s_data_clean = s_data["pages"]
    title_dict = {}
    for page in s_data_clean:
        title_dict[page["elements"][0]["name"]] = page["elements"][0]["title"]
    return title_dict


def load_results(uid):
    url_results = "https://dxsurvey.com/api/MySurveys/getSurveyResults/{}?accessKey={}".format(uid, accesskey)
    results = requests.get(url=url_results)
    results_json = results.json()
    return results_json


def load_survey(uid):
    url_survey = "http://api.dxsurvey.com/api/Survey/getSurvey?surveyId={}".format(uid)
    survey = requests.get(url=url_survey)
    survey_json = survey.json()
    return survey_json


def result_count(uid):
    data = load_results(uid)
    return data["ResultCount"]


# print(load_survey("e52c4e12-b1c0-41d7-b29c-61e8d3d61ba0"))
# print(load_results("e52c4e12-b1c0-41d7-b29c-61e8d3d61ba0"))
# print(get_titles("e52c4e12-b1c0-41d7-b29c-61e8d3d61ba0"))
# print(get_results_for_question(load_results("a60d46ab-75c2-42fe-81cb-acc0653855c9"), "question1"))