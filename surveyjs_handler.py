import requests


id = "7b8ea9b3-284d-42fb-b08a-09ceb317cf2e"
accesskey = "3bc43120cf784d489aefbc4cec9b1268"
url_get_results = "https://dxsurvey.com/api/MySurveys/getSurveyResults/{}?accessKey={}".format(id, accesskey)
url_get_survey = "http://api.dxsurvey.com/api/Survey/getSurvey?surveyId={}".format(id)
# url_create_survey = "https://dxsurvey.com/api/MySurveys/create?accessKey={}&name={}&ownerId={}".format(
#         accesskey, survey_name, owner_id)

def upload_survey():
    survey_name = "testupload"
    owner_id = ""
    url_create_survey = "https://dxsurvey.com/api/MySurveys/create?accessKey={}&name={}&ownerId={}".format(
        accesskey, survey_name, owner_id)
    temp_id = requests.get(url=url_create_survey)
    print(temp_id)

upload_survey()




