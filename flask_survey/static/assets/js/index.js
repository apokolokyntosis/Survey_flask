Survey.StylesManager.applyTheme("darkblue");

var surveyJSON = { surveyId: 'ee67b846-7a75-44af-9ea4-ab88714fde70'};

function sendDataToServer(survey) {
    survey.sendResult('001e5548-22c9-48e2-a577-e081733bb173');
}

var survey = new Survey.Model(surveyJSON);
$("#surveyContainer").Survey({
    model: survey,
    onComplete: sendDataToServer
});
