# import requests
#
# id = "7b8ea9b3-284d-42fb-b08a-09ceb317cf2e"
# accesskey = "3bc43120cf784d489aefbc4cec9b1268"
# url_results = "https://dxsurvey.com/api/MySurveys/getSurveyResults/{}?accessKey={}".format(id, accesskey)
# url_survey = "http://api.dxsurvey.com/api/Survey/getSurvey?surveyId={}".format(id)
#
#
# def get_questions():
#     data = load_data()
#     questions = []
#     first_dict = data["Data"][0]
#     for key in first_dict:
#         if key.startswith("question"):
#             questions.append(str(key))
#     return questions
#
#
# # parses values for a specific question into a list
# def parse_data(q):
#     data = load_data()
#     q_results = []
#     for entry in data["Data"]:
#         if "{}".format(q) in entry.keys():
#             q_results.append(str(entry[q]))
#     return q_results
#
#
# # parse survey_json for question titles -> returns dict with question
# # as key, and title as value
# def parse_survey():
#     survey = load_survey()
#     title_dict = {"question1": "Wie hat Ihnen die heutige Veranstaltung gefallen?",
#                   "question2pie": "Fühlen Sie sich ausreichend repräsentiert?",
#                   "question3pie": "Fühlen Sie sich ausreichend informiert?",
#                   "question4cloud": "Welchem Thema wurde ihrer Meinung\n nach noch nicht genug Beachtung geschenkt?"
#                   }
#     # for page in survey["pages"]:
#     #     title_dict[page[0]["elements"][0]["name"]] = page[0]["elements"][0]["title"]["de"]
#     #     print(title_dict)
#     return title_dict
#
#
# def load_data():
#     results = requests.get(url=url_results)
#     results_json = results.json()
#     return results_json
#
#
# def load_survey():
#     survey = requests.get(url=url_survey)
#     survey_json = survey.json()
#     return survey_json
#
#
# def result_count():
#     data = load_data()
#     return data["ResultCount"]



import requests

id = "7b8ea9b3-284d-42fb-b08a-09ceb317cf2e"
accesskey = "3bc43120cf784d489aefbc4cec9b1268"
url_survey = "http://api.dxsurvey.com/api/Survey/getSurvey?surveyId={}".format(id)


def get_questions(uid):
    data = load_data(uid)
    questions = []
    first_dict = data["Data"][0]
    for key in first_dict:
        if key.startswith("question"):
            questions.append(str(key))
    return questions


# parses values for a specific question into a list
def parse_data(q):
    data = load_data()
    q_results = []
    for entry in data["Data"]:
        if "{}".format(q) in entry.keys():
            q_results.append(str(entry[q]))
    return q_results


# parse survey_json for question titles -> returns dict with question
# as key, and title as value
def parse_survey():
    survey = load_survey()
    title_dict = {"question1": "Wie hat Ihnen die heutige Veranstaltung gefallen?",
                  "question2pie": "Fühlen Sie sich ausreichend repräsentiert?",
                  "question3pie": "Fühlen Sie sich ausreichend informiert?",
                  "question4cloud": "Welchem Thema wurde ihrer Meinung\n nach noch nicht genug Beachtung geschenkt?"
                  }
    # for page in survey["pages"]:
    #     title_dict[page[0]["elements"][0]["name"]] = page[0]["elements"][0]["title"]["de"]
    #     print(title_dict)
    return title_dict


def load_data(uid):
    url_results = "https://dxsurvey.com/api/MySurveys/getSurveyResults/{}?accessKey={}".format(uid, accesskey)
    results = requests.get(url=url_results)
    results_json = results.json()
    return results_json


def load_survey():
    survey = requests.get(url=url_survey)
    survey_json = survey.json()
    return survey_json


def result_count():
    data = load_data()
    return data["ResultCount"]
