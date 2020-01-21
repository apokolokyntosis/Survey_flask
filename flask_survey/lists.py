import requests

accesskey = "3bc43120cf784d489aefbc4cec9b1268"
url_results = "https://dxsurvey.com/api/MySurveys/getSurveyResults/{}?accessKey={}".format(id, accesskey)
url_survey = "http://api.dxsurvey.com/api/Survey/getSurvey?surveyId={}".format(id)


# gets a list of all active surveys on SurveyJS
def get_lists():
    url = "https://dxsurvey.com/api/MySurveys/getActive?accessKey={}&ownerId=".format(
        accesskey)
    response = requests.get(url=url)
    r_json = response.json()
    return r_json


