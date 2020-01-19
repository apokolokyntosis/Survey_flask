import requests
import json

# {Id: [A survey unique indentificator.], Json: [A new json string]}

accesskey = "3bc43120cf784d489aefbc4cec9b1268"
url_get_results = "https://dxsurvey.com/api/MySurveys/getSurveyResults/{}?accessKey={}".format(id, accesskey)

with open("survey_manual.json", "r") as read_file:
    survey_json = json.load(read_file)


def upload_survey(name):
    url_create_survey = "https://dxsurvey.com/api/MySurveys/create?accessKey={}&name={}&ownerId=".format(
        accesskey, name)
    response = requests.get(url=url_create_survey)
    json_response = response.json()
    id_new = json_response.get("Id")
    return id_new


def change_survey():
    url_change_survey = "https://dxsurvey.com/api/MySurveys/changeJson?accessKey={}".format(accesskey)
    response = requests.post(url=url_change_survey, json=post_survey_json)
    print(response.request.body)

id = upload_survey("test")

post_survey_json = {
  "Id": id,
  "Text": str(survey_json),
}

change_survey()


