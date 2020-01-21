import requests
import json

accesskey = "3bc43120cf784d489aefbc4cec9b1268"


# Creates a new survey on SurveyJS with name=name, and returns the ID of the newly created survey
def create_survey(name):
    url_create_survey = "https://dxsurvey.com/api/MySurveys/create?accessKey={}&name={}&ownerId=".format(
        accesskey, name)
    response = requests.get(url=url_create_survey)
    json_response = response.json()
    id_new = json_response.get("Id")
    return id_new


# Pushes the prepared post_survey_json to the respective survey on SurveyJS
def change_survey(post_survey_json):
    url_change_survey = "https://dxsurvey.com/api/MySurveys/changeJson?accessKey={}".format(accesskey)
    response = requests.post(url=url_change_survey, json=post_survey_json)
    print(response.request.body)


# Puts the created Survey json in the proper format for the API
def new_survey(name):
    with open("temp_survey.json", "r") as read_file:
        survey_json = json.load(read_file)
    id = create_survey(name)
    post_survey_json = {
        "Id": id,
        "Text": str(survey_json),
    }
    change_survey(post_survey_json)
